# users/forms.py

from django import forms
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    # Add custom validation if needed
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # You can add additional email validation logic here if needed
        return email
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise ValidationError("Password must be at least 6 characters.")
        return password
