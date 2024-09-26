from django.db import models
from cvApp.models import Cv
from commonApp.constants import TITLE_TYPE_CHOICES

class Title(models.Model):
	cv = models.OneToOneField(Cv, on_delete=models.CASCADE, related_name='title')
	type = models.CharField(max_length=50, blank=True, default=TITLE_TYPE_CHOICES[0])
	title = models.CharField(max_length=100, blank=True)
	details = models.CharField(max_length=1000, blank=True)
	linkedin_url = models.URLField(blank=True)
	other_url = models.URLField(blank=True)
	trimoji_url = models.URLField(blank=True)