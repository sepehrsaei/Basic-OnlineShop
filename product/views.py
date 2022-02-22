from django.shortcuts import render, redirect

from product.forms import ProductForm
from product.models import Category, Product


def home(request, id=None):
    if id is not None:
        cat = Category.objects.get(id=id)
        products = Product.objects.all().filter(category=cat)
    else:
        products = Product.objects.all()
    cats = Category.objects.all()
    context = {"products": products, "cats": cats}
    return render(request, 'home.html', context)


def product_list(request):
    if request.user.is_authenticated:
        return redirect("account:login")
    if not request.user.is_superuser:
        return redirect("home")
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "product_list.html", context)


def product_view(request, product_uuid):
    product = Product.objects.get(product_uuid=product_uuid)
    context = {"product": product}
    return render(request, 'product_view.html', context)


def product_edit(request, product_uuid):
    if not request.user.is_authenticated:
        return redirect("account:login")
    if not request.user.is_superuser:
        return redirect("home")
    products = Product.objects.all()
    p = Product.objects.get(product_uuid=product_uuid)
    if request.method == 'POST':
        p.available = request.POST["available"]
        p.price = request.POST["price"]
        p.save()
        return redirect("account:table", 1)
    else:
        context = {'products': products, "p": p}
        return render(request, 'product_edit.html', context)


def product_delete(request, product_uuid):
    if not request.user.is_authenticated:
        return redirect("account:login")
    if not request.user.is_superuser:
        return redirect("home")
    product = Product.objects.get(product_uuid=product_uuid)
    product.delete()
    return redirect("account:table")


def cat(request):
    cats = Category.objects.all()
    context = {"cats": cats}
    return render(request, 'cat_view.html', context)