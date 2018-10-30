from django.shortcuts import render


def emergency_room(request):
    return render(request, 'emergency-room.html')


def local_family_medical_practitioner(request):
    return render(request, 'local-family-medical-practitioner.html')


def login(request):
    if request.method == 'POST':
        pass
        # form = StripeForm(request.POST)
        # if form.is_valid():
        #     stripe_token = form.cleaned_data['stripeToken']
        #     user.is_subscribed = True
        #     payment = Payment()
        #     payment.price = price
        #     payment.stripe_email = form.cleaned_data['stripeEmail']
        #     payment.stripe_token = stripe_token
        #     payment.user = user
        #     charge = stripe.Charge.create(amount=price, currency='usd', description=description, source=stripe_token)
        #     payment.save()
        #     user.subscription_end_date_time = payment.date_time + timedelta(days=30)
        #     user.save()
        #     return redirect('application:profile')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        pass
        # form = StripeForm(request.POST)
        # if form.is_valid():
        #     stripe_token = form.cleaned_data['stripeToken']
        #     user.is_subscribed = True
        #     payment = Payment()
        #     payment.price = price
        #     payment.stripe_email = form.cleaned_data['stripeEmail']
        #     payment.stripe_token = stripe_token
        #     payment.user = user
        #     charge = stripe.Charge.create(amount=price, currency='usd', description=description, source=stripe_token)
        #     payment.save()
        #     user.subscription_end_date_time = payment.date_time + timedelta(days=30)
        #     user.save()
        #     return redirect('application:profile')
    else:
        return render(request, 'register.html')


def urgent_care(request):
    return render(request, 'urgent-care.html')
