# Generated by Django 3.2.8 on 2021-11-28 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_userinfo_back_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='national_code',
            field=models.IntegerField(default=0),
        ),
    ]
