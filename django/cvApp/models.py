from django.db import models
from authApp.models import CustomUser

class Cv(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cvs')
    name = models.CharField(max_length=50, blank=True, default="Nouveau CV")