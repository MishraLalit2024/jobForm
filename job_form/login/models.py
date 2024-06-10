from django.db import models

# Create your models here.


class UserLoginForm(models.Model):
    """Fields:"""
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=16, blank=False)
