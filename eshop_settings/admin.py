from django.contrib import admin

# Register your models here.
from eshop_settings.models import SiteSetting

admin.site.register(SiteSetting)
