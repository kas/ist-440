from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

# TODO create logout button in main menu
# TODO add register link to login screen
# TODO add main menu link to footer (if logged in)
# TODO use django login forms and user registration forms
# TODO set up insurance cards


@login_required
def emergency_room(request):
    return render(request, 'emergency-room.html')


@login_required
def local_family_medical_practitioner(request):
    return render(request, 'local-family-medical-practitioner.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('application:main-menu')
            else:
                form = LoginForm()
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('application:login')


@login_required
def main_menu(request):
    return render(request, 'main-menu.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            user = User()
            user.email = form.cleaned_data['email']
            user.password = form.cleaned_data['password']
            user.username = form.cleaned_data['username']
            user.save()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # TODO redirect to main menu
            else:
                form = RegisterForm()
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def urgent_care(request):
    return render(request, 'urgent-care.html')
