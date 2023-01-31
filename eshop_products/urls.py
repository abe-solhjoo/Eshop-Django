from django.urls import path

from .views import products, ProductsList

urlpatterns = [
    path('products-function', products),
    path('products', ProductsList.as_view()),
]