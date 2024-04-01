from django.shortcuts import render, redirect

from product.forms import ProductForm
from product.models import Product


def get_all_product(request):
    prod = Product.objects.all()
    return render(request, 'home.html', {'all_product': prod})


def get_one_product(request, id):
    p1 = Product.objects.get(pk=id)
    return render(request, "home.html", {'all_product': [p1]})


def create_data(request):
    p_form = ProductForm(request.POST)
    if p_form.is_valid():
        p_form.save()
        return redirect("index")
    return render(request, 'add.html', {'form': p_form})


def edit_data(request, id):
    prod = Product.objects.get(pk=id)
    if prod:
        p_form = ProductForm(request.POST, instance=prod)
        return render(request, 'edit.html', {'form': p_form, 'pid': prod.id})
    return redirect("index")


def update_data(request, id):
    prod = Product.objects.get(pk=id)
    if prod:
        p_form = ProductForm(request.POST, instance=prod)
        if p_form.is_valid():
            p_form.save()
            return redirect("index")
        else:
            return p_form.errors


def delete_data(request, id):
    pd = Product.objects.get(pk=id)
    pd.delete()
    return redirect("index")

