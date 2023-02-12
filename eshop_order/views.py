from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from eshop_order.forms import UserNewOrderForm
from eshop_order.models import Order
from eshop_products.models import Product


@login_required
def add_user_order(request):
    new_order_form = UserNewOrderForm(request.POST or None)

    if new_order_form.is_valid():
        order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id, is_paid=False)

        product_id = new_order_form.cleaned_data.get('product_id')
        count = new_order_form.cleaned_data.get('count')
        if count < 1:
            count = 1
        product = Product.objects.get_by_id(product_id=product_id)
        order.orderdetail_set.create(product_id=product.id, price=product.price, count=count)
        # todo: redirect user to user panel
        # return redirect('/user')
        return redirect(f'/products/{product.id}/{product.title.replace(" ","-")}')

    return redirect('/')
