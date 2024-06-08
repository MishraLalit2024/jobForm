from django import forms
from .models import Employees
from django.contrib.auth.forms import UserCreationForm


class EmployeesForm(UserCreationForm):
    """Form definition for Employees."""
    # phone = forms.TextInput(required=True)

    class Meta:
        """Meta definition for Employeesform."""

        model = Employees
        fields = ['username', 'first_name', 'last_name', 'phone', 'email',
                  'password1', 'password2', 'is_superuser']
        # labels = {'username': 'Username',
        #           'first_name': 'First Name',
        #           'last_name': 'Last Name',
        #           'password': 'Enter Password',
        #           'password': 'Confirm Password',
        #           'phone': 'Mobile Number',
        #           'email': 'Email Address',
        #           'is_superuser': 'Tick if registering as superuser.'}
        # widgets = {'username': forms.TextInput(
        #     attrs={'class': 'w-25 form-control'}),
        #     'first_name': forms.TextInput(
        #     attrs={'class': 'w-25 form-control'}),
        #     'last_name': forms.TextInput(
        #     attrs={'class': 'w-25 form-control'}),
        #     'password': forms.TextInput(
        #     attrs={'class': 'w-25 form-control'}),
        #     'password': forms.TextInput(
        #     attrs={'class': 'w-25 form-control'}),
        #     'phone': forms.TextInput(
        #     attrs={'class': 'w-25 form-control'}),
        #     'email': forms.TextInput(
        #     attrs={'class': 'w-25 form-control'}),
        #     'is_superuser': forms.CheckboxInput(
        #     attrs={'class': 'checkbox'})}
