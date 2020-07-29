from django.contrib import admin
from .models import Category, Product, Variation

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'id', 'name', 'slug', 'brief', 'status_category'
    )

    list_filter = (
        'id', 'name', 'slug', 'status_category'
    )

    search_fields = [
        'id', 'name', 'slug', 'status_category'
    ]


class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'id', 'name', 'image', 'price', 'brief', 'status_product', 'category',
    )

    list_filter = (
        'name', 'price', 'status_product', 'category',
    )

    search_fields = [
        'id', 'name', 'image', 'price', 'status_product',
    ]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
