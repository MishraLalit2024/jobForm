from django.urls import path
from .views import createForm, loginUser


urlpatterns = [
    path('', createForm, name='createLogin'),
    path('login', loginUser, name='postLogin')
]
