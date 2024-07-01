from django.db import models

from users.models import User


class NewProduct(models.Model):
    name = models.CharField(max_length=50, unique=True)
    new_description = models.TextField()
    new_price = models.DecimalField(max_digits=6, decimal_places=2)
    new_quantity = models.PositiveBigIntegerField(default=0)
    new_image_main = models.ImageField(upload_to='products_images', default='')
    new_image_addition = models.ImageField(upload_to='products_images', default='')

    class Meta:
        verbose_name = 'NewProduct'
        verbose_name_plural = 'NewProducts'

    def __str__(self):
        return self.name
    

