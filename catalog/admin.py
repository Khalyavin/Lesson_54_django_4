from django.contrib import admin

from catalog.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'photo', 'price', 'date_org', 'date_fill', )
    search_fields = ('name', 'description', )
