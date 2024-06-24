from django.contrib import admin
from .models import Wishlist
from .models import Bag, Product, Image, Catalog

class ImageInline(admin.TabularInline):
    model = Image
    extra = 4  # Количество дополнительных полей для загрузки изображений

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    fields = ('name', 'description', ('price', 'quantity'), ('image_main', 'image_add2', 'image_add3', 'image_add4', 'image_add5'), 'stripe_product_price_id', 'VRimage')
    search_fields = ('name',)
    ordering = ('name',)
    inlines = [ImageInline]
admin.site.register(Image)


class BagAdmin(admin.TabularInline):
    model = Bag
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0

class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']
admin.site.register(Wishlist, WishlistAdmin)

class CatalogAdmin(admin.ModelAdmin):
    pass
admin.site.register(Catalog, CatalogAdmin)
