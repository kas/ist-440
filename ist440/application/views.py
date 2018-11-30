from .forms import InsuranceCardForm, RegisterForm
from .models import InsuranceCard
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import redirect, render

# TODO set up registration form correctly (like login form)
# TODO fix register view (find better way to verify username doesn't already exist)


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
def confirm_delete_insurance_card(request, insurance_card_id):
    insurance_card = None
    try:
        insurance_card = InsuranceCard.objects.get(id=insurance_card_id)
    except:
        pass
    if not insurance_card or insurance_card.user != request.user:
        raise Http404
    return render(request, 'confirm-delete-insurance-card.html', {'insurance_card': insurance_card})


@login_required
def delete_insurance_card(request, insurance_card_id):
    insurance_card = None
    try:
        insurance_card = InsuranceCard.objects.get(id=insurance_card_id)
    except:
        pass
    if not insurance_card or insurance_card.user != request.user:
        raise Http404
    insurance_card.delete()
    return redirect('application:view-insurance-cards')


@login_required
def edit_insurance_card(request, insurance_card_id):
    insurance_card = None
    try:
        insurance_card = InsuranceCard.objects.get(id=insurance_card_id)
    except:
        pass
    if not insurance_card or insurance_card.user != request.user:
        raise Http404
    if request.method == 'POST':
        form = InsuranceCardForm(request.POST)
        if form.is_valid():
            insurance_card.company = form.cleaned_data['company']
            insurance_card.first_name = form.cleaned_data['first_name']
            insurance_card.last_name = form.cleaned_data['last_name']
            insurance_card.middle_name = form.cleaned_data['middle_name']
            insurance_card.number = form.cleaned_data['number']
            insurance_card.save()
            return redirect('application:view-insurance-cards')
    else:
        form = InsuranceCardForm(instance=insurance_card)
    return render(request, 'edit-insurance-card.html', {'form': form, 'insurance_card_id': insurance_card.id})


@login_required
def emergency_room(request):
    return render(request, 'emergency-room.html')


@login_required
def end(request):
    return render(request, 'end.html')


@login_required
def local_family_medical_practitioner(request):
    return render(request, 'local-family-medical-practitioner.html')


@login_required
def main_menu(request):
    return render(request, 'main-menu.html')


@login_required
def need_medical_assistance(request):
    return render(request, 'need-medical-assistance.html')


@login_required
def new_insurance_card(request):
    if request.method == 'POST':
        form = InsuranceCardForm(request.POST)
        if form.is_valid():
            insurance_card = InsuranceCard()
            insurance_card.company = form.cleaned_data['company']
            insurance_card.first_name = form.cleaned_data['first_name']
            insurance_card.last_name = form.cleaned_data['last_name']
            insurance_card.middle_name = form.cleaned_data['middle_name']
            insurance_card.number = form.cleaned_data['number']
            insurance_card.user = request.user
            insurance_card.save()
            return redirect('application:view-insurance-cards')
    else:
        form = InsuranceCardForm()
    return render(request, 'new-insurance-card.html', {'form': form})


@login_required
def question_1(request):
    return render(request, 'question-1.html')


@login_required
def question_2(request):
    return render(request, 'question-2.html')


@login_required
def question_3(request):
    return render(request, 'question-3.html')


@login_required
def urgent_care(request):
    return render(request, 'urgent-care.html')


@login_required
def view_insurance_cards(request):
    insurance_cards = InsuranceCard.objects.filter(user=request.user)
    return render(request, 'view-insurance-cards.html', {'insurance_cards': insurance_cards})
