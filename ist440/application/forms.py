from .models import InsuranceCard
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class InsuranceCardForm(ModelForm):
    class Meta:
        model = InsuranceCard
        fields = ['company', 'first_name', 'middle_name', 'last_name', 'number']


class RegisterForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']
