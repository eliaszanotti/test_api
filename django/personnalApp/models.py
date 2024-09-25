from django.db import models
from cvApp.models import Cv
from django.core.exceptions import ValidationError
from commonApp.constants import LICENSE_CHOICES

def validate_age(value):
	if value < 0 or value > 150:
		raise ValidationError("Age must be between 0 and 150")

def validate_postal_code(value):
	if not value.isdigit() or len(value) != 5:
		raise ValidationError("Postal code must be a 5-digit number")

class Personnal(models.Model):
	cv = models.OneToOneField(Cv, on_delete=models.CASCADE, related_name='personnal')
	picture = models.ImageField(upload_to='pictures/', null=True, blank=True, default="")
	is_hidden = models.BooleanField(default=False)
	name = models.CharField(max_length=50, blank=True)
	first_name = models.CharField(max_length=50, blank=True)
	phone = models.CharField(max_length=20, blank=True)
	email = models.EmailField(max_length=254, blank=True)
	age = models.IntegerField(validators=[validate_age], null=True, blank=True)
	birthdate = models.DateField(null=True, blank=True)
	additional = models.CharField(max_length=50, blank=True)
	postal_code = models.CharField(validators=[validate_postal_code], max_length=10, blank=True)
	city = models.CharField(max_length=50, blank=True)
	country = models.CharField(max_length=50, blank=True)
	license = models.CharField(max_length=50, blank=True, default=LICENSE_CHOICES[0])
	other_license = models.CharField(max_length=50, blank=True)
	has_vehicle = models.BooleanField(default=False)
	range = models.CharField(max_length=100, blank=True)