from django.shortcuts import render, redirect
from eshop_slider.models import Slider
from eshop_settings.models import SiteSetting


# header cod behind
def header(request, *args, **kwargs):
    context = {

    }
    return render(request, 'shared/Header.html', context)


# header cod behind
def footer(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()

    context = {
        'setting': site_setting
    }
    return render(request, 'shared/Footer.html', context)


def home_page(request):
    sliders = Slider.objects.all()
    context = {
        'data': "new data",
        'sliders': sliders
    }
    return render(request, 'home_page.html', context)
