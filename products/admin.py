from django.contrib import admin

# Register your models here.
from .models import Product, Review, Brand, Category

# class ProductAdminInline(admin.TabularInline):
#     model = Brand

# admin.site.register(Product,inlines=[ProductAdminInline])
admin.site.register(Review)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)

