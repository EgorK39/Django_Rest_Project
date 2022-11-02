from django.db import models


# from django.contrib.auth import get_user_model

# from django.contrib.auth.models import User

# User = get_user_model()


class RegisterView(models.Model):
    phone = models.CharField(max_length=12, blank=False)
    login = models.CharField(max_length=24, blank=False)
    password = models.CharField(max_length=24, blank=False)
    name = models.CharField(max_length=18, blank=False)
    birth = models.DateField(blank=False)
    tg = models.CharField(max_length=24, blank=True)
    email = models.EmailField(blank=True)

# Create your models here.
