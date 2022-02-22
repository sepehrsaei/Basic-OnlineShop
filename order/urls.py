from django.urls import path

from order import views

app_name = 'order'
urlpatterns = [
    path('orders-list/<int:customer>', views.orders_list, name="orders_list"),
    path('order-view/<uuid:order_uuid>', views.order_view, name="order_view"),
    path("order-delete/<uuid:order_uuid>", views.order_delete, name="order_delete"),
    path("order-edit/<uuid:order_uuid>", views.order_edit, name="order_edit"),
    path("order-list/", views.order_list, name="order_list"),
]