# Generated by Django 3.2.8 on 2021-10-25 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_userinfo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/user/'),
        ),
    ]