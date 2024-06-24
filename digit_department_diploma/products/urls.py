from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import HomePageView, SearchResultsView
from . import views

urlpatterns = [
    path('',  views.CatalogListView.as_view(), name='catalog'),
    path('product_page/<int:product_id>/', views.ProductListView.as_view(), name='product_page'),
    path('wishlist', login_required(views.WishlistView.as_view()), name='wishlist'),
    path('wishlist/add/<int:product_id>/', views.wishlist_add, name='wishlist_add'),
    path('wishlist/remove/<int:wishlist_item_id>/', views.wishlist_remove, name='wishlist_remove'),
    path('bag', login_required(views.BagView.as_view()), name='bag'),
    path('bag/add/<int:product_id>/', views.bag_add, name='bag_add'),
    path('bag/remove/<int:bag_id>/', views.bag_remove, name='bag_remove'),
    path('bag/minus/<int:bag_id>/', views.bag_minus, name='bag_minus'),
    path('bag/plus/<int:bag_id>/', views.bag_plus, name='bag_plus'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
]