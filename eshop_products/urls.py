from django.urls import path

from .views import products, ProductsList, product_detail, SearchProductsView, ProductsListByCategory, \
    products_categories_partial

urlpatterns = [
    path('products-function', products),
    path('products', ProductsList.as_view()),
    path('products/search', SearchProductsView.as_view()),
    path('products/<category_name>', ProductsListByCategory.as_view()),
    path('products/<productId>/<name>', product_detail),
    path('products_category_partial', products_categories_partial, name='products_categories_partial'),
]
