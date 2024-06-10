from django.urls import path
from .views import registerUser, createForm

urlpatterns = [
    path('', createForm, name='form'),
    path('createUser', registerUser, name='postData'),
]
