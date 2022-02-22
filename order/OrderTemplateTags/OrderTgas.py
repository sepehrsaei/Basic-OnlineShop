from django import template

from account.models import UserInfo
from order.models import Order
from product.models import Category

register = template.Library()


@register.simple_tag
def get_userinfo(user_id):
    return UserInfo.objects.get(user_id=user_id)


@register.simple_tag
def get_categories():
    return Category.objects.all()


@register.simple_tag
def get_order_price(order_id):
    price = 0
    for p in Order.objects.get(id=order_id).product.all():
        price += p.price
    return price
