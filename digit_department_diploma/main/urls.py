from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('', views.home, name='home'),
    path('', include('products.urls')),
    path('search/', views.search, name='search'),
]
