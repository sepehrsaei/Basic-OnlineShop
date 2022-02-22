from django.contrib import admin

from order.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ("user_uuid", "created_date", "is_closed", "status", "payment")
    list_filter = ("is_closed", "payment", "status")
    search_fields = ("order_id",)


admin.site.register(Order, OrderAdmin)
