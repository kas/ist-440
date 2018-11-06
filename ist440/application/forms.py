from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    email = forms.EmailField(label='Email address', max_length=255)
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=255, widget=forms.PasswordInput)
