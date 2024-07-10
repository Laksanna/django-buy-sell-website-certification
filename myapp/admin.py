from django.contrib import admin
from .models import Product
# Register your models here.

admin.site.site_header="Buy and Sell Website"


class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','desc')
    search_fields=('name',)


    list_editable=('price','desc')

admin.site.register(Product,ProductAdmin)