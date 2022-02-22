from django.contrib import admin

from account.models import UserInfo


class UserInformation(admin.ModelAdmin):
    list_display = ("user_uuid", "user_id", "phone")
    search_fields = ("user_uuid",)


admin.site.register(UserInfo, UserInformation),
