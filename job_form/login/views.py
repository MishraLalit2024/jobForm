from django.shortcuts import render, HttpResponse
from .form import LoginForm
from register.models import Employees
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def createForm(request):
    form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def loginUser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form_email = form.cleaned_data.get('email')
            form_password = form.cleaned_data.get('password')
            user = authenticate(email=form_email, password=form_password)
            print(user)
            if user is not None:
                user = login(request, user)
                request.session['user-email'] = form_email
                employee = Employees.objects.filter(email=form_email)
                request.session['user_id'] = employee[0].id
                request.session.set_expiry(60*15)
                request.session.save()
                return HttpResponse('<h1>Hello World!</h1>')
            else:
                html = "{% url 'form' %}"
                return HttpResponse(f'<h4>Invalid Login Attempt or User do not exist. Try again or register again.</h4><br><br><a href="register/">Register here.</a>')
