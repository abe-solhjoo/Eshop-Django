from django.urls import path

from .views import products, ProductsList, product_detail, SearchProductsView

urlpatterns = [
    path('products-function', products),
    path('products', ProductsList.as_view()),
    path('products/<productId>/<name>', product_detail),
    path('products/search', SearchProductsView.as_view()),
]

