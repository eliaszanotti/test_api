from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    current_cv = models.OneToOneField('cvApp.Cv', null=True, blank=True, on_delete=models.SET_NULL, related_name='current_user')