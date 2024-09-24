from django.db import models
from django.conf import settings

class Cv(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cvs')
    name = models.CharField(max_length=50, blank=True, default="Nouveau CV")