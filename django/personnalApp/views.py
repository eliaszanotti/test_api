from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.views import APIView
from commonApp.views import BaseGetView, BaseUpdateGenericView
from .models import Personnal
from commonApp.constants import LICENSE_CHOICES
import os, uuid

class PersonnalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Personnal
		fields = '__all__'

class PersonnalGetView(BaseGetView):
	serializer_class = PersonnalSerializer
	model = Personnal

	def get(self, request, *args, **kwargs):
		response = super().get(request, *args, **kwargs)
		response.data['license_choices'] = LICENSE_CHOICES
		return response

class PersonnalUpdateView(BaseUpdateGenericView):
	serializer_class = PersonnalSerializer
	model = Personnal

class PersonnalPictureUpdateView(APIView):
	def put(self, request, *args, **kwargs):
		try:
			user = request.user
			cv = user.current_cv
			personnal = Personnal.objects.get_or_create(cv=cv)[0]
			if 'picture' in request.FILES:
				if personnal.picture:
					personnal.picture.delete()
				new_picture = request.FILES['picture']
				extension = os.path.splitext(new_picture.name)[1]
				new_filename = f"{uuid.uuid4()}{extension}"
				new_picture.name = new_filename
				personnal.picture = new_picture
				personnal.save()
				return Response({'success': 'Picture updated'}, status=status.HTTP_200_OK)
			return Response({'error': 'No picture provided'}, status=status.HTTP_400_BAD_REQUEST)
		except ValidationError as error:
			return Response(error.message_dict, status=status.HTTP_400_BAD_REQUEST)
		except Personnal.DoesNotExist:
			return Response({'error': 'Personnal not found'}, status=status.HTTP_404_NOT_FOUND)