from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, username, referral_id, password=None):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, referral_id=referral_id, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, username, referral_id, password=None):
        user = self.create_user(email, first_name, last_name, username, referral_id, password)
        user.is_staff = True
        user.is_verified = True
        user.is_superuser = True
        user.is_active = True
    
        user.save(using=self._db)
        return user



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    username = models.CharField(max_length=60, unique=True)
    verification_code = models.CharField(max_length=10, blank=True, null=True)
    verification_token = models.CharField(max_length=100, blank=True, null=True)
    verification_token_created_at = models.DateTimeField(null=True, blank=True)
    referral_id = models.CharField(max_length=10, unique=True)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'referral_id']

    objects = CustomUserManager()

    

User = get_user_model()

class Referral(models.Model):
    referred_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='referral')
    referrer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='referrals')
    created_at = models.DateTimeField(default=timezone.now)
