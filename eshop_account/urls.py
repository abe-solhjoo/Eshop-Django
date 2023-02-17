from django.urls import path

from eshop_account.views import login_user, register, log_out, user_account_main_page, edit_user_profile

urlpatterns = [
    path('login', login_user),
    path('log-out', log_out),
    path('user', user_account_main_page),
    path('user/edit-profile', edit_user_profile),
    path('register', register)
]