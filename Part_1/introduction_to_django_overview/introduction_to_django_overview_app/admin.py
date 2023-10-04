from django.contrib import admin
from .models import Product, Company

# Register your models here.

admin.site.register(Company)
admin.site.register(Product)


# Create super user to enter admin panel
# You can use this command after migration
# 