from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import account
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include("account.urls")),
    path('product/', include("product.urls")),
    path('', views.home, name="home"),
    path('order/', include("order.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

