from django import forms
from django.db import models
class NameForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)
    # name = forms.CharField(label='Username', max_length=100)
    # your_name = forms.CharField(label='Your name', max_length=100)

class OrderName(forms.Form):
    products_name = forms.CharField(label='Username', max_length=100)
    books = forms.CharField(label='Books', max_length=100)
    title = forms.CharField(label='Title', max_length=100)
    # price = models.FloatField(label='Price', null=True)
 
  
  