from django.urls import path

from eshop_order.views import add_user_order

urlpatterns = [
    path('add-user-order', add_user_order)
]
