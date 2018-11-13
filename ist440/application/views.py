from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

# TODO set up insurance cards
# TODO set up registration form correctly (like login form)
# TODO fix register view (find better way to verify username doesn't already exist)


@login_required
def emergency_room(request):
    return render(request, 'emergency-room.html')


@login_required
def local_family_medical_practitioner(request):
    return render(request, 'local-family-medical-practitioner.html')


@login_required
def main_menu(request):
    return render(request, 'main-menu.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = None
            try:
                user = User.objects.get(username=username)
            except:
                pass
            if user is not None:
                form = RegisterForm()
            else:
                user = User.objects.create_user(username, form.cleaned_data['email'], form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('application:main-menu')
                else:
                    form = RegisterForm()
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def urgent_care(request):
    return render(request, 'urgent-care.html')
