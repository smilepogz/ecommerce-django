from django.contrib import admin

# Register your models here.
from django.contrib import admin

# # Register your models here.
from .models import Products
from .models import Books
admin.site.register(Books)

admin.site.register(Products)