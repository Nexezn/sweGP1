from django.urls import path
from cart.views import add_to_cart, cart, checkout

app_name = 'cart'

urlpatterns = [
    path('', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('<int:pk>/', add_to_cart, name= 'add_to_cart'),
]