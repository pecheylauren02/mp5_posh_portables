from django.contrib import admin
from .models import Product, Category

# Model Registration
admin.site.register(Product)
admin.site.register(Category)
