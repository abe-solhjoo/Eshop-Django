from django import forms
from django.contrib.auth.models import User
from django.core import validators


class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد نمایید'}),
        label='نام کاربری',
        validators=[
            validators.MaxLengthValidator(limit_value=20, message='تعداد کاراکتر های وارد شده می بایست کمتر از 20 باشد')
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه ی عبور خود را وارد نمایید'}),
        label='کلمه ی عبور'
    )


class RegisterForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'place_holder': 'لطفا نام کاربری را وارد نمایید'}),
        label='نام کاربری'
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'place_holder': 'لطفا ایمیل خود را وارد نمایید'}),
        label='ایمیل'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'place_holder': 'لطفا پسورد خود را وارد نمایید'}),
        label='پسورد'
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'place_holder': 'لطفا تکرار پسورد خود را وارد نمایید'}),
        label='تکرار پسورد'
    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        if_exists_user_by_username = User.objects.filter(username=user_name).exists()

        if if_exists_user_by_username:
            raise forms.ValidationError('نام کاربری وارد شده قبلا استفاده شده است')
        return user_name

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('پسورد های وارد شده برابر نمی باشند')

        return password
