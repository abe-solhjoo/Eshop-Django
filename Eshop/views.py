from django.shortcuts import render, redirect


# header cod behind
def header(request, *args, **kwargs):
    context = {

    }
    return render(request, 'shared/Header.html', context)


# header cod behind
def footer(request, *args, **kwargs):
    context = {
        'about_us': 'ما در حال توسعه هستیم'
    }
    return render(request, 'shared/Footer.html', context)


def home_page(request):
    context = {
        'data': "new data"
    }
    return render(request, 'home_page.html', context)
