from django.contrib import admin

from new_products.models import NewProduct

@admin.register(NewProduct)
class NewProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'new_price', 'new_quantity')
    fields = ('name', 'new_description', ('new_price', 'new_quantity'), ('new_image_main', 'new_image_addition'))
    search_fields = ('name',)
    ordering = ('name',)
