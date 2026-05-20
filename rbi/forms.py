from django import forms
from django.forms import inlineformset_factory
from django.contrib.auth.forms import AuthenticationForm

class DateInput(forms.DateInput):
    input_type = 'date'
    input_formats = ['%Y-%m-%d']

class LoginForm(AuthenticationForm):
    username=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    password=forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )

