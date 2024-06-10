from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Employees(AbstractUser):
    phone = models.CharField(max_length=15, blank=False, unique=True)
    email = models.EmailField(unique=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']
