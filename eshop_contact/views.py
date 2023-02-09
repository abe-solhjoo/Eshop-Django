from django.shortcuts import render

from eshop_settings.models import SiteSetting
from .models import ContactUs

# Create your views here.
from eshop_contact.forms import CreateContactForm


def contact_page(request):
    contact_form = CreateContactForm(request.POST or None)

    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get('full_name')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        text = contact_form.cleaned_data.get('text')

        ContactUs.objects.create(full_name=full_name, email=email, subject=subject, text=text, is_read=False)
        # todo: show users success massage
        contact_form = CreateContactForm()

    site_setting = SiteSetting.objects.first()

    context = {
        'contact_form': contact_form,
        'setting': site_setting
    }
    return render(request, 'contact_us/contact_us_page.html', context)
