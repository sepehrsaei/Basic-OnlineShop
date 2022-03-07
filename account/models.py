import uuid
from django.contrib.auth.models import User
from django.db import models


class UserInfo(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    user_uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    image = models.ImageField(upload_to="media/user/")
    phone = models.CharField(max_length=11)
    national_code = models.IntegerField(default=0)
    back_money = models.IntegerField(default=0)
    address = models.TextField(blank=True, null=True)
    firla = models.CharField(default='', max_length=20)
