from django.urls import path

from .views import products, ProductsList, product_detail

urlpatterns = [
    path('products-function', products),
    path('products', ProductsList.as_view()),
    path('products-detail', product_detail),
]