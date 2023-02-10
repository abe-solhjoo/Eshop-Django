from django import forms


class UserNewOrderForm(forms.Form):
    productId = forms.CharField(
        widget=forms.TextInput()
    )

    count = forms.IntegerField(
        widget=forms.NumberInput(),
        initial=1
    )
