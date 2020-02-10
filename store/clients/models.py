from django.db import models
import datetime
from django.utils import timezone
from django import forms

class Products(models.Model):
    products_name = models.CharField(max_length=200)
    product_image = models.ImageField( null=True, blank=True)
    objects = models.Manager()
    
    def __str__(self):
        return self.products_name
class Books(models.Model):
    # title = models.ForeignKey(Products, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.FloatField(null=True,)
    # book_image = models.ImageField(null=True, blank=True)
    # objects = models.Manager()
    def __str__(self):
        return self.title

