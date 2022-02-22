from django.urls import path

from product import views

app_name = 'product'
urlpatterns = [
    path('cat/', views.cat, name="category"),
    path('cat/<int:id>/', views.home, name="cat-list"),
    path('product-list/', views.product_list, name="product_list"),
    path('product-edit/<uuid:product_uuid>', views.product_edit, name="product_edit"),
    path('product-delete/<uuid:product_uuid>', views.product_delete, name="product_delete"),
    path('product-view/<uuid:product_uuid>', views.product_view, name="product_view"),
]