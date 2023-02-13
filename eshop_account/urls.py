from django.urls import path

from eshop_account.views import login_user, register, log_out

urlpatterns = [
    path('login', login_user),
    path('log-out', log_out),
    path('register', register)
]