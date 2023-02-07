from django.shortcuts import render


# Create your views here.

def contact_page(request):
    context = {

    }
    return render(request, 'contact_us/contact_us_page.html', context)
