from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product


def index(request):
    '''return HttpResponse("<h4>проверка работы</h4>")'''
    return render(request, 'main/main.html')


def catalog(request):
    return HttpResponse("<h4>каталог товаров</h4>")


def basket(request):
    return HttpResponse("<h4>корзина товаров</h4>")


def wishlist(request):
    return HttpResponse("<h4>избранное</h4>")

def home(request):
    return render(request, 'home.html')

def search(request):
    if request.method == 'POST':
        query = request.POST.get('search_query')
        results = Product.objects.filter(name__icontains=query)
        return render(request, 'search.html', {'results': results})
    else:
        return render(request, 'search.html')


