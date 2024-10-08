from django.db import models
from cvApp.models import Cv

class Settings(models.Model):
	cv = models.OneToOneField(Cv, on_delete=models.CASCADE, related_name='settings')
	template = models.IntegerField(default=0)
	experience_first = models.BooleanField(default=True)
	primary_color = models.CharField(max_length=7, blank=True)
	secondary_color = models.CharField(max_length=7, blank=True)
	third_color = models.CharField(max_length=7, blank=True)
	dark_color = models.CharField(max_length=7, blank=True)
	light_color = models.CharField(max_length=7, blank=True)
	size = models.CharField(max_length=50, blank=True)