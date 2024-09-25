from commonApp.views import BaseGetView, BaseUpdateGenericView
from .models import Personnal
from rest_framework import serializers

class PersonnalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Personnal
		fields = '__all__'

class PersonnalGetView(BaseGetView):
	serializer_class = PersonnalSerializer
	model = Personnal

	def get(self, request, *args, **kwargs):
		response = super().get(request, *args, **kwargs)
		response.data['license_choices'] = Personnal.LICENSE_CHOICES
		return response

class PersonnalUpdateView(BaseUpdateGenericView):
	serializer_class = PersonnalSerializer
	model = Personnal