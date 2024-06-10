from django import forms
from .models import UserLoginForm


class LoginForm(forms.ModelForm):
    class Meta:
        model = UserLoginForm
        fields = ['email', 'password']
        labels = {'email': 'Email-Address',
                  'password': 'Password'}
        widgets = {'email': forms.EmailInput(
            attrs={'type': 'email', 'class': 'w-25 form-control', 'placeholder': 'Email Address'}),
            'password': forms.TextInput(attrs={'type': 'password', 'class': 'w-25 form-control', 'placeholder': 'Enter Password'})}
