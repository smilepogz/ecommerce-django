from django.http import HttpResponse
from django.shortcuts import render
from .models import Products, Books
from django.http import HttpResponseRedirect
from .forms import NameForm
from .forms import OrderName

def products(request):
    products = Products.objects.all()   
    return render(request,'clients/dashboard_products.html',{'products':products})

def product_detail(request, product_id ):
    product = Products.objects.get(id=product_id)
    
    # return render(request, 'clients/books_order.html',{'product':product,
    # 'categories':categories} )
    return render(request, 'clients/books_order.html',{'product':product})


def add(request):
   
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
        
            return HttpResponseRedirect('../../')
     
    else:
        form = NameForm()

        return render(request, 'clients/login.html', {'form': form})


def login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('../../')
            #   return render(request,'clients/dashboard_products.html')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

        return render(request, 'clients/login.html', {'form': form})
