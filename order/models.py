import uuid
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

from product.models import Product


class Order(models.Model):
    STATUS = (
        (1, 'Shop Store'),
        (2, 'Post'),
        (3, 'Delivered')
    )
    Payment = (
        (1, 'Cash'),
        (1, 'Cash On Delivery'),
    )

    order_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user_uuid = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    is_closed = models.BooleanField(default=False)
    status = models.SmallIntegerField(choices=STATUS, default=1)
    payment = models.SmallIntegerField(choices=Payment, default=1)
    created_date = models.DateTimeField(default=datetime.now, blank=True)