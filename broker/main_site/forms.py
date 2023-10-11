from django import forms
from django.core.validators import MinLengthValidator
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password(8 or more characters)'}),
        validators=[
            MinLengthValidator(limit_value=8, message="Password must be at least 8 characters long.")
        ]
    )

    referred_by = forms.CharField(
        required=False,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Referrer (Optional)'})
    )
    
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'username', 'password', 'referral_id', 'referred_by']
        labels = {
            'referral_id': '',
            'email': '',
            'first_name': '',
            'last_name': '',
            'username': '',
            'password': '',
        }
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add placeholders for form fields
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['referral_id'].widget.attrs['placeholder'] = 'Referral ID'
       


class CustomUserLoginForm(forms.Form):
    email = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Email'}),
       
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        
    )



class CustomUserVerifyEmail(forms.Form):
    verification_code = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Enter code sent to your Email'})
       
    )


class ContactForm(forms.Form):
    name = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'})
       
    )

    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your Email'})
    )

    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'placeholder': 'Type message',
            'rows': 4,
             'cols': 50
            })
       
    )
