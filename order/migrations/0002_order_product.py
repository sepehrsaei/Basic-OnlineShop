# Generated by Django 3.2.8 on 2021-11-08 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(to='product.Product'),
        ),
    ]
