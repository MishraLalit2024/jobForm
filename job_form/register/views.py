from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .form import EmployeesForm

# Create your views here.


def createForm(request):
    form = EmployeesForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def registerUser(request):
    if request.method == 'POST':
        print('Reached Here.')
        form = EmployeesForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.set_password(form.cleaned_data.get('password'))
            instance.save()
            return HttpResponse('Success')
    else:
        return HttpResponse('Lose!')
