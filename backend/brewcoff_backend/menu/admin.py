from django.contrib import admin
from .models import Category, MenuItem, Modifier


# Register models ke admin panel
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description'] # kolom yang di tampilkan di list
    search_fields = ['name']

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'base_price', 'is_available'] # kolom yang di tampilkan
    list_filter = ['category', 'is_available'] # filter sidebar
    search_fields = ['name', 'description'] # bisa search

@admin.register(Modifier)
class ModifierAdmin(admin.ModelAdmin):
    list_display = ['menu_item', 'modifier_type', 'option_name', 'price_adjustment']
    list_filter = ['modifier_type']
