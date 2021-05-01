from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class User (AbstractBaseUser):
    email = models.EmailField(verbose_name = 'email', max_Length=60, unique = True)
    username = models.CharField(max_Length=30, unique = True)
    