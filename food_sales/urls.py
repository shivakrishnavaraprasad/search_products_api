from django.urls import path
from .views import search_product_orders

urlpatterns = [
    path('orders/', search_product_orders),
]