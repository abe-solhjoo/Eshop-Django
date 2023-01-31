from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
from django.http import Http404


# Create your views here.

def products(request):
    context = {

    }
    return render(request, 'products/products_list.html', context)


class ProductsList(ListView):
    template_name = 'products/products_list.html'

    # This is for paging
    paginate_by = 6

    queryset = Product.objects.get_active_products()


def product_detail(request, *args, **kwargs):
    product_id = kwargs['productId']

    product = Product.objects.get_by_id(product_id)
    if product is None:
        raise Http404('محصول مورد نظر یافت نشد')
    if product.active:
        context = {
            'product': product
        }
        return render(request, 'products/product_detail.html', context)
    raise Http404('محصول مورد نظر یافت نشد')

