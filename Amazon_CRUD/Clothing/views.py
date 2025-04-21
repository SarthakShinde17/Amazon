from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            fm = ProductForm()
    else:
        fm = ProductForm()

        
    prod = Product.objects.all()
    form = ProductForm()
    return render(request, 'Clothing/home.html', {'prod': prod , 'form': form})

def update_data(request, id):
    if request.method == 'POST':
        pi = Product.objects.get(pk=id)
        form = ProductForm(request.POST, request.FILES, instance=pi)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        pi = Product.objects.get(pk=id)
        form = ProductForm(instance=pi)
    return render(request, 'Clothing/update.html', {'form': form})

def delete_data(request, id):
    if request.method == 'POST':
        pi = Product.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    else:
        pi = Product.objects.get(pk=id)
    return render(request, 'Clothing/delete.html', {'pi': pi})