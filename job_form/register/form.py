from django import forms
from .models import Employees
from django.contrib.auth.forms import UserCreationForm


class EmployeesForm(forms.ModelForm):
    """Form definition for Employees."""
    # phone = forms.TextInput(required=True)

    class Meta:
        """Meta definition for Employeesform."""

        model = Employees
        fields = ['first_name', 'last_name', 'phone', 'email',
                  'password', 'is_superuser']
        labels = {'first_name': 'First Name',
                  'last_name': 'Last Name',
                  'password': 'Password',
                  'phone': 'Mobile Number',
                  'email': 'Email Address',
                  'is_superuser': 'Tick if registering as superuser.'}
        widgets = {'first_name': forms.TextInput(
            attrs={'class': 'w-25 form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(
            attrs={'class': 'w-25 form-control', 'placeholder': 'Last Name'}),
            'password': forms.TextInput(
            attrs={'class': 'w-25 form-control', 'placeholder': 'Enter Password'}),
            'phone': forms.TextInput(
            attrs={'class': 'w-25 form-control', 'placeholder': 'Mobile Number'}),
            'email': forms.EmailInput(
            attrs={'class': 'w-25 form-control', 'placeholder': 'Email Address'}),
            'is_superuser': forms.CheckboxInput(
            attrs={'class': 'checkbox mx-4'})}
