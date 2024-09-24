from django.db import models
from cvApp.models import Cv

class Personnal(models.Model):
	cv = models.OneToOneField(Cv, on_delete=models.CASCADE, related_name='personnal')
	# picture = models.ImageField(upload_to='pictures/', null=True, blank=True, default="")
	is_hidden = models.BooleanField(default=False)
	name = models.CharField(max_length=50, blank=True)
	first_name = models.CharField(max_length=50, blank=True)
	phone = models.CharField(max_length=20, blank=True)
	# email = EmailField(max_length=254, blank=True)
	# age = AgeField(null=True)
	# birthdate = DateField(max_length=10, blank=True)
	additional = models.CharField(max_length=50, blank=True)
	# postal_code = PostalCodeField(null=True)
	city = models.CharField(max_length=50, blank=True)
	country = models.CharField(max_length=50, blank=True)
	# license = models.CharField(max_length=50, default=LICENSE_CHOICES[0])
	other_license = models.CharField(max_length=50, blank=True)
	has_vehicle = models.BooleanField(default=False)
	range = models.CharField(max_length=100, blank=True)