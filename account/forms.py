
from django import forms

from account.models import UserInfo


class UserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['image']