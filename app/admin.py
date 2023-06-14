from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price', 'selling_price', 'category', 'product_image']
    filter = ['title']
    list_editable = ['discounted_price', 'selling_price']
