from django.urls import path
from .views import products_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', products_page, name = 'product_page'),
    
]
