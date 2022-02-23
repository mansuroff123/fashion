from django.contrib import admin
from django.utils.safestring import mark_safe

from .forms import ColorModelForm
from.models import *

@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_filter = ['created_at']


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_filter = ['created_at']
    autocomplete_fields = ['tag', 'category']

@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']

@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'color', 'created_at']
    list_display_links = ['id', 'code']
    form = ColorModelForm

    def color(self, obj):
        return mark_safe(f"<div style='width: 20px; height=20px; background:{obj};></div>")

@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']