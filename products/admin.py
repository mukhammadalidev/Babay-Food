from django.contrib import admin
from  .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image']
    list_filter = ('name', 'price', 'image')
    search_fields = ('name', 'price', 'image')


admin.site.register(Product, ProductAdmin)