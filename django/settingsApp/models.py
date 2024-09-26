from django.db import models
from cvApp.models import Cv
from commonApp.constants import SETTINGS_FONT_SIZES_CHOICES
from .schemes import TEMPLATES

class Settings(models.Model):
	cv = models.OneToOneField(Cv, on_delete=models.CASCADE, related_name='settings')
	template = models.IntegerField(default=0)
	experience_first = models.BooleanField(default=True)
	primary_color = models.CharField(max_length=7, blank=True, default=TEMPLATES[0]['primary'][0])
	secondary_color = models.CharField(max_length=7, blank=True, default=TEMPLATES[0]['secondary'][0])
	third_color = models.CharField(max_length=7, blank=True, default=TEMPLATES[0]['third'][0])
	dark_color = models.CharField(max_length=7, blank=True, default=TEMPLATES[0]['dark'][0])
	light_color = models.CharField(max_length=7, blank=True, default=TEMPLATES[0]['light'][0])
	size = models.CharField(max_length=50, blank=True, default=SETTINGS_FONT_SIZES_CHOICES[0])