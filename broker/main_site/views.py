from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import CustomUserCreationForm, CustomUserLoginForm, CustomUserVerifyEmail, ContactForm
from .models import CustomUser, Referral
from random import choices
from django.http import HttpResponse
from django.utils import timezone
from .currencies import get_tickers
import json

VERIFICATION_CODE_NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



def home(request):

  if request.user.is_authenticated:
    return redirect('dashboard')
    
  return render(request, 'main_site/home.html')


def home_page(request):

    
  return render(request, 'main_site/home.html')

def about(request):
  return render(request, 'main_site/about.html')


def services(request):
  return render(request, 'main_site/services.html')


def legal_terms(request):
  return render(request, 'main_site/terms.html')


def contact(request):
 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():          
            name = form.cleaned_data['name'].title()
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
    
            
            subject = 'New Contact Form Submission'
            message = f'Name: {name}\nEmail: {email}\nMessage: {message}'
            from_email = email 
            recipient_list = ['foliocoins@gmail.com']  
            
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            success_message = 'Send Successful!!'
          
            return render(request, 'main_site/contact.html', {
              'form': form,
              'message': success_message
              })
    
    else:
        form = ContactForm()
    
    return render(request, 'main_site/contact.html', {'form': form})


@login_required(login_url="login")
def transaction_history(request):

  return render(request, 'main_site/transaction.html')


@login_required(login_url="login")
def bonus(request):
  
  return render(request, 'main_site/bonus.html')


@login_required(login_url="login")
def loan(request):
  
  return render(request, 'main_site/loan.html')


@login_required(login_url="login")
def user_account(request):
  
  return render(request, 'main_site/user.html')


@login_required(login_url="login")
def dashboard_view(request):
  try:
    tickers = get_tickers()
    
  
  except Exception as e:
     response = HttpResponse(status=505)
  
  else:

    return render(request, 'main_site/dashboard.html', {'tickers': tickers})

  return render(request, 'main_site/dashboard.html')



def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if not form.is_valid():
            email = request.POST.get('email')
            username = request.POST.get('username')
            try:
              unverified_user = CustomUser.objects.get(email=email)
              
              if unverified_user.is_verified == False:
                unverified_user.delete()
                return redirect('sign-up')
            except CustomUser.DoesNotExist:
              pass
                      
       
        if form.is_valid():
                
            user = form.save(commit=False)
            user.email = form.cleaned_data['email'].lower()
            user.referral_id = form.cleaned_data['referral_id'].title()
            user.first_name = form.cleaned_data['first_name'].title()
            user.last_name = form.cleaned_data['last_name'].title()
             
            user.set_password(form.cleaned_data['password'])
            
            code = ''.join(str(number) for number in choices(VERIFICATION_CODE_NUMBERS, k=6))
            
            referred_by = request.POST.get('referred_by').title()

            if referred_by != '':
              try:
            
                referrer = CustomUser.objects.get(referral_id=referred_by)
                referrer_id = referrer.referral_id
               
                request.session['referrer_id'] = referrer_id
              except CustomUser.DoesNotExist:
                not_found = f'Referrer with ID "{referred_by}" not found!!'
                return render(request, 'registration/sign_up.html', {
                  'form': form,
                  'not_found': not_found
                  })

            if CustomUser.objects.filter(referral_id=user.referral_id).exists():
              error_message = f'Referral ID "{user.referral_id}" already in use. Please choose a different one.'
              return render(request, 'registration/sign_up.html', {
                'form': form, 
                'error_message': error_message
                })
            
            

            user.verification_token_created_at = timezone.now()
            user.save()
            request.session['code'] = code
            user_id = user.id
            request.session['user_id'] = user_id
            
            subject = 'Verify your email'
            message = f'Your verification code is {code}'
            from_email = 'foliocoins@gmail.com'
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            
            return redirect(f'verify_email')

    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/sign_up.html', {'form': form})


def verify_email(request):
    user_id = request.session['user_id']
    user = get_object_or_404(CustomUser, pk=user_id) 
    if request.method == 'POST':
        form = CustomUserVerifyEmail(request.POST)
        if form.is_valid():
            gen_code = request.session['code']
            entered_code = form.cleaned_data['verification_code']
            if entered_code == gen_code:
                user.is_verified = True
                user.is_active = True
                user.save()
                del request.session['code']

                if 'referrer_id' in request.session:
                    referral_id = request.session['referrer_id']
                    referrer = CustomUser.objects.get(referral_id=referral_id)
                    Referral.objects.create(referred_user=user, referrer=referrer)
                    del request.session['referrer_id']
                
                del request.session['user_id']
                login(request, user)
                response_data = {
                    'success': True,
                    'redirect_url': 'dashboard'  
                }
                return JsonResponse(response_data)
            else:
                message = 'Incorrect Verification code'
                response_data = {
                    'success': False,
                    'message': message
                }
                return JsonResponse(response_data)
        else:
            response_data = {
                'success': False,
                'message': 'Form is not valid'
            }
            return JsonResponse(response_data)
    else:
        form = CustomUserVerifyEmail()
        return render(request, 'registration/verify.html', {'form': form})


def login_view(request):
   
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email'].lower()
            password = form.cleaned_data['password']
            
            user = authenticate(request, email=email, password=password)

            if user is not None:
              if user.is_verified:
                login(request, user)
                
                return redirect('dashboard')

            else:
                message = 'Invalid email or password.'
                return render(request, 'registration/login.html', {
                  'form': form,
                  'message': message
                  })
 
    else:
        form = CustomUserLoginForm()

    return render(request, 'registration/login.html', {'form': form})



def logout_view(request):
  if request.user.is_authenticated:
    logout(request)

  return redirect('home')
  