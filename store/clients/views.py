from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import Products

from .forms import NameForm, OrderForm

def products(request):
    products = Products.objects.all()   
    return render(request,'clients/dashboard_products.html',{'products':products})

def product_detail(request, product_id ):
    product = Products.objects.get(id=product_id)
    
    # return render(request, 'clients/books_order.html',{'product':product,
    # 'categories':categories} )
    context =   {'product':product}
    return render(request, 'clients/books_order.html',context)

def create_order(request):
       form = OrderForm()
       if request.method == 'POST':
        #    print('Printing POST:', request.POST)
            form = OrderForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/')
       context = {'form':form}
       return render(request, 'clients/order_form.html', context)

def update_order(request, pk):
    order = Products.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        #    print('Printing POST:', request.POST)
            form = OrderForm(request.POST, request.FILES, instance=order)
            if form.is_valid():
                form.save()
                return redirect('/')
       
    context = {'form':form}
    return render(request, 'clients/order_form.html', context)

def delete_order(request, pk):
    order = Products.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'item':order}
    return render(request, 'clients/delete.html', context)

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
