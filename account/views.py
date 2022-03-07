import os

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.files.images import ImageFile

from account.forms import UserForm
from account.models import UserInfo
from order.models import Order
from product.models import Product


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('account:login')
    if request.user.is_superuser:
        return render(request, 'dashboard.html')
    else:
        return redirect("account:profile")


def table(request, state):
    if not request.user.is_authenticated:
        return redirect('account:login')
    if state == 1:
        products = Product.objects.all()
        context = {"products": products, "state": state}
        return render(request, 'tables.html', context)
    elif state == 2:
        admins = User.objects.all().filter(is_superuser=True)
        context = {'admins': admins, "state": state}
        return render(request, 'tables.html', context)
    elif state == 3:
        pass
    elif state == 4:
        customers = User.objects.all().filter(is_superuser=False)
        context = {"customers": customers, "state": state}
        return render(request, 'tables.html', context)
    elif state == 5:
        customers = User.objects.all().filter(is_superuser=False)
        context = {"customers": customers, "state": state}
        return render(request, "tables.html", context)
    else:
        pass
    return redirect("account:login")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.save()
            UserInfo(user_id=user).save()
            return redirect("account:login")
        return render(request, "register.html")
    else:
        return render(request, "register.html")


def log_in(request):
    if request.user.is_authenticated:
        return redirect("account:dashboard")
    else:
        if request.method == "POST":
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                if request.user.is_superuser:
                    return redirect("account:dashboard")
                else:
                    return redirect("account:profile")
            return render(request, "login.html")
        else:
            return render(request, 'login.html')


def profile(request):
    if request.user.username == ("admin"):
        return redirect("account:dashboard")
    if not request.user.is_authenticated:
        return redirect("account:login")
    else:
        user = User.objects.get(id=request.user.id)
        info = UserInfo.objects.get(user_id=user)
        context = {'userinfo': info}
        return render(request, "profile.html", context)


def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = User.objects.get(id=request.user.id)
            user.email = request.POST['email']
            user.save()
            info = UserInfo.objects.get(user_id=user)
            info.firla = request.POST['firla']
            info.phone = request.POST['phone']
            info.national_code = request.POST['national_code']
            info.save()
            return redirect('account:profile')
        user = User.objects.get(id=request.user.id)
        info = UserInfo.objects.get(user_id=user)
        context = {'userinfo' : info}
        return render(request, 'edit_profile.html', context)
    else:
        return redirect('account:login')


def upload_image(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user = User.objects.get(id=request.user.id)
            old_image = UserInfo.objects.get(user_id=user)
            form = UserForm(request.POST, request.FILES, instance=old_image)
            if form.is_valid():
                # deleting old uploaded image.
                # image_path = old_image.image.path
                # if os.path.exists(image_path):
                #     os.remove(image_path)
                # the `form.save` will also update your newest image & path.
                form.save()
                return redirect("account:profile")
            return redirect("account:profile")
        return redirect("account:edit_profile")
    return redirect('account:login')


def log_out(request):
    logout(request)
    return redirect("home")


def admin_view(request, user_id):
    if not request.user.is_authenticated:
        return redirect("account:login")
    if not request.user.is_superuser:
        return redirect("account:profile")
    user = User.objects.get(id=user_id)
    context ={'user': user}
    return render(request, 'admin_view.html', context)


def customer_view(request, user_uuid):
    if not request.user.is_authenticated:
        return redirect("account:login")
    if not request.user.is_superuser:
        return redirect("account:profile")
    user_info = UserInfo.objects.get(user_uuid=user_uuid)
    user = User.objects.get(id=user_info.user_uuid)
    context = {"user": user, "user_info": user_info}
    return render(request, "customer_view.html", context)


def add_to_cart(request, product_uuid):
    if not request.user.is_authenticated:
        return redirect("account:login")
    user = User.objects.get(id=request.user.id)
    order = Order.objects.filter(user_uuid=user).last()
    product = Product.objects.get(product_uuid=product_uuid)
    if order:
        order.product.add(product)
    else:
        order = Order.objects.create(user_uuid=user)
        order.product.add(product)
    return redirect("order:order_list")

