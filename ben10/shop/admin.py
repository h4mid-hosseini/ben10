from django.contrib import admin
from .models import Product


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'owner',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    search_fields = ('name', 'id')

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}
