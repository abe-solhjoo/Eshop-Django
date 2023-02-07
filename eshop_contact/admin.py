from django.contrib import admin

# Register your models here.
from eshop_contact.models import ContactUs


class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'subject', 'is_read']
    list_filter = ['is_read']


admin.site.register(ContactUs, ContactAdmin)
