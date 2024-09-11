from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админ-зона Продуктов."""
    list_display = (
        'name',
        'description',
        'price'
    )
    search_fields = (
        'name',
        'description',
    )
    list_display_links = (
        'name',
    )
    list_editable = (
        'price',
    )
