from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('products', views.get_products, name='get_all_products'),
    path('products/<str:code>', views.get_product, name='get_one_product'),
    path('create', views.create_product, name='create_product'),
    path('update/<str:code>', views.update_product, name='update_product')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)