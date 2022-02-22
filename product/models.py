import uuid

from django.db import models


class Product(models.Model):
    RATES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    name = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='media/product/')
    published_at = models.DateTimeField()
    product_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    details = models.TextField()
    company = models.CharField(max_length=255)
    available = models.IntegerField()
    rate = models.IntegerField(default=0, choices=RATES)
    price = models.DecimalField(max_digits=5, decimal_places=0)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name