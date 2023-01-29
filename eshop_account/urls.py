from django.urls import path

from eshop_account.views import login_user, register

urlpatterns = [
    path('login', login_user),
    path('register', register)
]