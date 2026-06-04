from django.urls import path
from .views import login_page, registration_page, logout_page, cart_page, add_cart, delete_from_cart, update_quantity

urlpatterns = [
    path('login/', login_page, name='login_page'),
    path('registration/', registration_page, name='registration_page'),
    path('logout/', logout_page, name='logout'),
    path('cart/', cart_page, name = 'cart_page'),
    path('cart/<int:pid>', add_cart, name = 'add_cart'),
    path('cart/delete/<int:item_id>', delete_from_cart, name='delete_from_cart'),
    path('cart/update/<int:item_id>', update_quantity, name='update_quantity'),
]