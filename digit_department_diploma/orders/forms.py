from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'login__input', 'placeholder': 'имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'login__input', 'placeholder': 'фамилия'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'login__input', 'placeholder': 'страна'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'login__input', 'placeholder': 'город'}))
    postal_code = forms.CharField(widget=forms.NumberInput(
        attrs={
            'class': 'login__input',
            'placeholder': 'почтовый индекс'
        }
    ))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'login__input', 'placeholder': 'адрес'}))
    phone = forms.CharField(widget=forms.NumberInput(attrs={'class': 'login__input', 'placeholder': 'телефон'}))

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'country', 'city', 'postal_code', 'address', 'phone')