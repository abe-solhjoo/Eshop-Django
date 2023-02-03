from django.contrib import admin

# Register your models here.
from eshop_products_category.models import ProductCategory


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name']

    class Meta:
        model = ProductCategory


admin.site.register(ProductCategory, ProductCategoryAdmin)
