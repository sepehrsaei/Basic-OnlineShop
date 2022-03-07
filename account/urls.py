from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from account import views

app_name = "account"
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('table/<int:state>/', views.table, name="table"),
    path('register/', views.register, name="register"),
    path('login/', views.log_in, name="login"),
    path('edit-profile/', views.edit_profile, name="edit_profile"),
    path('logout/', views.log_out, name="delete"),
    path('upload_image', views.upload_image, name="upload_image"),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.log_out, name='log_out'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('customer-view/<uuid:user_uuid>', views.customer_view, name='customer_view'),
    path('add-to-cart/<uuid:product_uuid>', views.add_to_cart, name='add_to_cart')
]
