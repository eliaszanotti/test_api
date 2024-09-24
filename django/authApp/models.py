from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    current_cv = models.IntegerField(default=1)