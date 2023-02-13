from django.contrib import admin

# Register your models here.
from eshop_order.models import Order, OrderDetail


class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_paid']
    list_filter = ['is_paid']


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'order']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
