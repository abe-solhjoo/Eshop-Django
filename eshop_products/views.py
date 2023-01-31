from django.shortcuts import render
from django.views.generic import ListView
from .models import Product


# Create your views here.

def products(request):
    context = {

    }
    return render(request, 'products/products_list.html', context)


class ProductsList(ListView):
    template_name = 'products/products_list.html'

    queryset = Product.objects.get_active_products()