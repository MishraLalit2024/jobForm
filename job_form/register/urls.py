from django.urls import path
from .views import registerUser, loginfunc, createForm

urlpatterns = [
    path('register', createForm, name='form'),
    path('createUser', registerUser, name='postData'),
    path('login', loginfunc, name='login')
]
