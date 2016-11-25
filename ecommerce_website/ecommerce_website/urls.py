"""ecommerce_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from ecommerce import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ec/list/', views.index),
    url(r'^ec/cart_add/(?P<product_id>[0-9]+)/', views.cart_add),
    url(r'^ec/cart_delete/(?P<product_id>[0-9]+)/', views.cart_delete),
    url(r'^ec/cart_reset/', views.cart_reset),
    url(r'^ec/cart_list/', views.cart_list),
    url(r'^ec/order/', views.order),
    url(r'^ec/order_execute/', views.order_execute),
    url(r'^ec/order_complete/', views.order_complete)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
