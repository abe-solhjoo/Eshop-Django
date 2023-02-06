from django.shortcuts import render, redirect
from eshop_slider.models import Slider


# header cod behind
def header(request, *args, **kwargs):
    context = {

    }
    return render(request, 'shared/Header.html', context)


# header cod behind
def footer(request, *args, **kwargs):
    context = {
        'about_us': "این سایت جهت پروژه دانشگاهی توسط ابراهیم صلح جو ایجاد گردیده است."
    }
    return render(request, 'shared/Footer.html', context)


def home_page(request):
    sliders = Slider.objects.all()
    context = {
        'data': "new data",
        'sliders': sliders
    }
    return render(request, 'home_page.html', context)
