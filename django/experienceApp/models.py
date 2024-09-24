from django.db import models
from cvApp.models import Cv

class Experience(models.Model):
	cv = models.ForeignKey(Cv, on_delete=models.CASCADE, related_name='experiences')
	start_month = models.CharField(max_length=50, blank=True)
	start_year = models.IntegerField(null=True)
	end_month = models.CharField(max_length=50, blank=True)
	end_year = models.IntegerField(null=True)
	is_current = models.BooleanField(default=False)
	company = models.CharField(max_length=100, blank=True)
	title = models.CharField(max_length=100, blank=True)
	city = models.CharField(max_length=100, blank=True)
	contract = models.CharField(max_length=50, blank=True)
	details = models.TextField(blank=True)
	order = models.PositiveIntegerField(null=True, blank=True, editable=False)