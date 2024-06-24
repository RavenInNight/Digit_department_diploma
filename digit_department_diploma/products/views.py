from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Wishlist
from django.shortcuts import render, redirect
from .forms import ProductForm, ProductImageForm

# from common.views import TitleMixin

from .models import Bag, Product


class TitleMixin:
    title = 'None'

    def get_context_data(self, **kwargs):
        context = super(TitleMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context


class CatalogListView(TitleMixin, ListView):
    model = Product
    template_name = 'products/shop.html'
    title = 'магазин'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CatalogListView, self).get_context_data()
        context['products'] = Product.objects.all()
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        product_id = self.kwargs.get('product_id')
        context['title'] = Product.objects.filter(id=product_id).first().name.lower()
        context['product'] = Product.objects.get(id=product_id)
        return context

    def post(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        if self.request.user.is_authenticated:
            product = Product.objects.get(id=product_id)
            wishlist_item, created = Wishlist.objects.get_or_create(user=self.request.user, product=product)
            if created:
                # Добавлено в избранное
                return redirect('wishlist')
            else:
                # Уже в избранном
                return redirect('product', product_id=product_id)
        else:
            # Пользователь не аутентифицирован
            return redirect('login')  # Перенаправление на страницу входа


class BagView(TitleMixin, TemplateView):
    template_name = 'products/bag.html'
    title = 'корзина'


@login_required
def bag_add(request, product_id):
    product = Product.objects.get(id=product_id)
    bags = Bag.objects.filter(user=request.user, product=product)

    if not bags.exists():
        Bag.objects.create(user=request.user, product=product, quantity=1)
    else:
        bag = bags.first()
        bag.quantity += 1
        bag.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def bag_remove(request, bag_id):
    bag = Bag.objects.get(id=bag_id)
    bag.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def bag_minus(request, bag_id):
    bag = Bag.objects.get(id=bag_id)
    if bag.quantity == 1:
        bag.delete()
    else:
        bag.quantity -= 1
        bag.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def bag_plus(request, bag_id):
    bag = Bag.objects.get(id=bag_id)
    product = Product.objects.get(id=bag.product_id)

    if product.quantity > bag.quantity:
        bag.quantity += 1
        bag.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class WishlistView(TitleMixin, TemplateView):
    model = Wishlist
    template_name = 'products/wishlist.html'
    title = 'избранное'

    def get_context_data(self, **kwargs):
        context = super(WishlistView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            wishlist_items = Wishlist.objects.filter(user=self.request.user)
            context['wishlist_items'] = wishlist_items
        return context


@login_required
def wishlist_add(request, product_id):
    product = Product.objects.get(id=product_id)
    wishlist_item = Wishlist.objects.filter(user=request.user, product=product)

    if not wishlist_item.exists():
        Wishlist.objects.create(user=request.user, product=product, quantity=1)
    else:
        wishlist = wishlist_item.first()
        wishlist.quantity += 1
        wishlist.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def wishlist_remove(request, wishlist_item_id):
    wishlist_item = Wishlist.objects.get(id=wishlist_item_id)
    wishlist_item.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def add_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        image_form = ProductImageForm(request.POST, request.FILES)
        if product_form.is_valid() and image_form.is_valid():
            product = product_form.save()
            image = image_form.save(commit=False)
            image.product = product
            image.save()
            return redirect('product_detail', pk=product.pk)
    else:
        product_form = ProductForm()
        image_form = ProductImageForm()
    return render(request, 'add_product.html', {'product_form': product_form, 'image_form': image_form})


def wishlist_view(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'title': 'Избранное', 'wishlist': wishlist})


def show_wishlist(request):
    products_wishlist = Wishlist.objects.all()

    for item in products_wishlist:
        print(item.product_id)  # Вывод данных на консоль

    return render(request, 'wishlist.html', {'products_wishlist': products_wishlist})


from django.views.generic import TemplateView, ListView

from .models import Product


class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Product
    template_name = 'search_results.html'
