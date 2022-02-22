# import form as form
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

import order
from order.models import Order
from product.models import Product
from account.models import UserInfo


def order_list(request):
    if not request.user.is_authenticated:
        return redirect("account:login")
    if not request.user.is_superuser:
        return redirect("home")
    orders = Order.objects.all()
    context={"orders": orders}
    return render(request, "order_list.html", context)


# def order_view(request, order_uuid):
#     order =Order.objects.get(order_uuid=order_uuid)
#     context = {'order': order}
#     return render(request, "order/order_view.html", context)


def check_list(request, order_id):
    return list(set(form).intersection(order))


def order_edit(request, order_uuid):
    if not request.user.is_authenticated:
        return redirect("account:login")
    if not request.user.is_superuser:
        return redirect("home")
    order = Order.objects.get(order_uuid=order_uuid)
    if request.method == 'POST':
        products = Order.product.all()
        products_ids = [p.id for p in products]
        products_form = request.POST['products']
        cmn = check_list(products_ids, products_form)

        must_delete = list(set(products_ids) - set(cmn))
        for pr_id in must_delete:
            mahsol = Product.objects.get(id=pr_id)
        order.product.remove(mahsol)
        return redirect("order:order_view", order.order_uuid)
    else:
        context = {'order': order}
        return render(request, 'order_edit.html', context)


def orders_list(request, customer):
    if not request.user.is_authenticated:
        return redirect("account:login")
    if not request.user.is_superuser:
        return redirect("home")
    user_info = UserInfo.objects.get(user_id=customer)
    customer = User.objects.get(id=customer)
    orders = Order.objects.all().filter(user_uuid=customer)
    context = {'orders': orders, 'user_info': user_info, "customer": customer}
    return render(request, "order_list.html", context)


def order_view(request, order_uuid):
    if not request.user.is_authenticated:
        return redirect('account:login')
    order = Order.objects.get(order_uuid=order_uuid)
    user_info = User.objects.get(id=order.user_uuid.id)
    context = {'order': order, 'user_info': user_info}
    return render(request, 'orderu_view.html', context)


def order_delete(request, order_uuid):
    if not request.user.is_authenticated:
        return redirect("account:login")
    if not request.user.is_superuser:
        return redirect("home")
    order = Order.objects.get(order_uuid=order_uuid)
    order.delete()
    return render(request, "orderu_view.html")