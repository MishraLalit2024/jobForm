from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .form import EmployeesForm
from django.contrib import messages

# Create your views here.


def createForm(request):
    form = EmployeesForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def registerUser(request):
    if request.method == 'POST':
        form = EmployeesForm(request.POST)
        # print(request.POST)
        # print(form.fields.keys)
        # print(form.fields.values)
        # print(form.is_valid())
        # if form.is_valid():
        print(form)
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Account created for {username}!')
        return HttpResponse('Success')
    # else:
        # return HttpResponse('Lose!')


def loginfunc(request):
    return HttpResponse('hello')
