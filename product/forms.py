from django import forms

from product.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'image',
            'price',
            'details',
            'company',
            'category',
            'published_at',
            'available',
        ]
