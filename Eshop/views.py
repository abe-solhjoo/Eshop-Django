import itertools

from django.shortcuts import render, redirect

from eshop_products.models import Product
from eshop_slider.models import Slider
from eshop_settings.models import SiteSetting


# header cod behind
def header(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }
    return render(request, 'shared/Header.html', context)


# header cod behind
def footer(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()

    context = {
        'setting': site_setting
    }
    return render(request, 'shared/Footer.html', context)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def home_page(request):
    related_products = Product.objects.get_queryset().distinct()

    grouped_related_products = my_grouper(3, related_products)

    sliders = Slider.objects.all()
    context = {
        'data': "new data",
        'sliders': sliders,
        'grouped': grouped_related_products
    }
    return render(request, 'home_page.html', context)


def about_page(request):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }

    return render(request, 'about_page.html', context)
