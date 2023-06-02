from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full py-4 rounded-md',
        'placeholder': 'Your Name'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full py-4 rounded-md',
        'placeholder': 'Your Password'
    }))

#https://stackoverflow.com/questions/44691003/how-can-change-the-border-radius-of-the-the-input-text-filed-created-by-django-f

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full py-4 rounded-md',
        'placeholder': 'Your Name'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'w-full py-4 rounded-md',
        'placeholder': 'Your Email Address'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full py-4 rounded-md',
        'placeholder': 'Your Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full py-4 rounded-md',
        'placeholder': 'Repeat Password'
    }))

class UpdateProfile(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
