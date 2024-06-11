from django.urls import path
from .views import create_form, show_form_data

urlpatterns = [
    path('', create_form, name='applicaton_from'),
    path('login/', show_form_data, name="thank")
]
