from django.urls import path

from eshop_contact.views import contact_page

urlpatterns = [
    path('contact-us', contact_page)
]
