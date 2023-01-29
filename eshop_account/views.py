from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import login, get_user_model, authenticate


# Create your views here.

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    login_form = LoginForm(request.POST or None)

    if login_form.is_valid():
        user_name = login_form.cleaned_data.get('user_name')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=user_name, password=password)
        print(user)
        print(login_form.cleaned_data)

        if user is not None:
            login(request, user)
            return redirect('/')

    context = {
        'login_form': LoginForm

    }

    return render(request, 'account/login.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    context = {

    }
    return render(request, 'account/register.html', context)
