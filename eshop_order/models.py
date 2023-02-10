from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from eshop_products.models import Product


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(verbose_name='پرداخت شده')
    payment_date = models.DateField(blank=True, null=True, verbose_name='تاریخ پرداخت')

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'

    def __str__(self):
        return self.owner.get_full_name()


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصولات')
    price = models.IntegerField(verbose_name='قیمت محصول')
    count = models.IntegerField(verbose_name='تعداد')

    class Meta:
        verbose_name = 'جزئیات محصول'
        verbose_name_plural = 'اطلاعات جزئیات محصولات'

    def __str__(self):
        return self.product.title