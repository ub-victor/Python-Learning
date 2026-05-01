from django.contrib import admin
# Import the Product model from the current app's models.py
from .models import Product 

# Register the Product model with the admin site so it can be managed through the Django admin interface
admin.site.register(Product) 