import uuid
from datetime import timedelta

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.timezone import now

from .models import User


class UsersLoginFrom(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'login__input', 'placeholder': 'имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'login__input', 'placeholder': 'пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'login__input', 'placeholder': 'имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'login__input', 'placeholder': 'фамилия'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'login__input', 'placeholder': 'имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'login__input', 'placeholder': 'почта'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'login__input', 'placeholder': 'пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'login__input',
            'placeholder': 'подтвердите пароль'
        }
    ))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=True)
        expiration = now() + timedelta(hours=24)
        return user