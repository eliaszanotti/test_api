from django.db import models
from cvApp.models import Cv

class Hobbie(models.Model):
	cv = models.ForeignKey(Cv, on_delete=models.CASCADE, related_name='hobbies')
	type = models.CharField(max_length=100, blank=True)
	name = models.CharField(max_length=100, blank=True)
	details = models.TextField(blank=True)
	duration = models.CharField(max_length=100, blank=True)
	order = models.PositiveIntegerField(null=True, blank=True, editable=False)