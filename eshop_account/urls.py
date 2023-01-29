from django.urls import path

from eshop_account.views import login, register

urlpatterns = [
    path('login', login),
    path('register', register)
]