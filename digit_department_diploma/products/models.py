import stripe

from django.db import models
from django.conf import settings

from users.models import User

stripe.api_key = settings.STRIPE_SECRET_KEY


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=0)
    quantity = models.PositiveIntegerField(default=0)
    image_main = models.ImageField(upload_to='products_images', default='')
    image_add2 = models.ImageField(upload_to='products_images', default='')
    image_add3 = models.ImageField(upload_to='products_images', default='')
    image_add4 = models.ImageField(upload_to='products_images', default='')
    image_add5 = models.ImageField(upload_to='products_images', default='')
    stripe_product_price_id = models.CharField(max_length=128, null=True, blank=True)
    VRimage = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.stripe_product_price_id:
            stripe_product_price = self.create_stripe_product_price()
            self.stripe_product_price_id = stripe_product_price['id']
        super(Product, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def create_stripe_product_price(self):
        stripe_product = stripe.Product.create(name=self.name)
        stripe_product_price = stripe.Price.create(
            product=stripe_product['id'], unit_amount=round(self.price * 100), currency='rub')
        return stripe_product_price


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'


class BagQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(bag.sum() for bag in self)

    def total_quantity(self):
        return sum(bag.quantity for bag in self)

    def stripe_products(self):
        line_items = []
        for bag in self:
            item = {
                'price': bag.product.stripe_product_price_id,
                'quantity': bag.quantity,
            }
            line_items.append(item)
        return line_items


class Bag(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BagQuerySet.as_manager()

    def __str__(self):
        return f'Bag for {self.user.username} | Product: {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity

    def de_json(self):
        basket_item = {
            'product_name': self.product.name,
            'quantity': self.quantity,
            'price': float(self.product.price),
            'sum': float(self.sum()),
        }
        return basket_item

    @classmethod
    def create_or_update(cls, product_id, user):
        bags = Bag.objects.filter(user=user, product_id=product_id)

        if not bags.exists():
            obj = Bag.objects.create(user=user, product_id=product_id, quantity=1)
            is_created = True
            return obj, is_created
        else:
            basket = bags.first()
            basket.quantity += 1
            basket.save()
            is_crated = False
            return basket, is_crated


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'Wishlist for {self.user.username} | Product: {self.product.name}'

    def de_json(self):
        wishlist_item = {
            'product_name': self.product.name,
            'user': self.user.username,
        }
        return wishlist_item

    @classmethod
    def add_to_wishlist(cls, product_id, user):
        wishlist_item, created = Wishlist.objects.get_or_create(user=user, product_id=product_id)
        return wishlist_item, created


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    file = models.ImageField(upload_to='images/')


class Catalog(models.Model):
    name = models.CharField(max_length=250)

