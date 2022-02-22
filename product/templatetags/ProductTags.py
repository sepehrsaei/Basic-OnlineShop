from django import template

from account.models import UserInfo
from order.models import Order

register = template.Library()


@register.simple_tag
def product_in_order(user_id):
    # u = UserInfo.objects.get(user_id=user_id)
    order = Order.objects.all().filter(user_uuid=user_id).filter(is_closed=False)
    if order:
        return order[0]
    else:
        return []


@register.simple_tag
def total_price(order_uuid):
    order = Order.objects.get(id=order_uuid)
    total = 0
    for product in order.product.all():
        total += product.price
    return {'total': total}
