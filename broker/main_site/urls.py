from django.contrib import admin
from django.urls import path
from .views import home, about, services, legal_terms, contact, register, verify_email, login_view, logout_view, transaction_history, dashboard_view, bonus, loan, user_account, home_page

urlpatterns = [
    path('', home, name='home'),
    path('/', home_page, name='home_page'),
    path('about', about),
    path('services', services),
    path('legal-terms', legal_terms),
    path('contact', contact, name='contact'),
    path('dashboard/transaction', transaction_history, name='transaction'),
    path('dashboard/bonus', bonus, name='bonus'),
    path('dashboard/loan', loan, name='loan'),
    path('user-account', user_account, name='user-account'),
    path('dashboard', dashboard_view, name='dashboard'),
    path('sign-up', register, name='sign-up'),
    path('verify_email/<int:user_id>/<str:token>/<str:referral_id>', verify_email, name='verify_email'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
]