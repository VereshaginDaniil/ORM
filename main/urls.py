from django.contrib import admin
from django.urls import path

from phones.views import show_product, show_catalog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', show_catalog, name='show_catalog'),
    path('catalog/<slug:slug>/', show_product, name='show_product'),
]
