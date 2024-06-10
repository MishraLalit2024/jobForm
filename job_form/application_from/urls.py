from django.urls import path
from .views import create_form

urlpatterns = [
    path('', create_form, name='applicaton_from')
]
