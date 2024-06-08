from django.urls import path
from .views import registerUser, loginfunc, createForm

urlpatterns = [
    path('', createForm, name='form'),
    path('register', registerUser, name='postData'),
    path('login', loginfunc, name='login')
]
