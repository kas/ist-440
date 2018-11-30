from .models import InsuranceCard
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class EmailForm(ModelForm):
    class Meta:
        fields = ['email']
        model = User


class InsuranceCardForm(ModelForm):
    class Meta:
        fields = ['company', 'first_name', 'middle_name', 'last_name', 'number']
        model = InsuranceCard


class PasswordForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ['password']
        model = User


class RegisterForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ['email', 'username', 'password']
        model = User


class UsernameForm(ModelForm):
    class Meta:
        fields = ['username']
        model = User
