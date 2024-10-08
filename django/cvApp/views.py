from rest_framework import serializers, generics
from .models import Cv
from django.contrib.auth import get_user_model

User = get_user_model()

class CvSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())

	class Meta:
		model = Cv
		fields = '__all__'

class CvCreateView(generics.CreateAPIView):
	serializer_class = CvSerializer

	def perform_create(self, serializer):
		cv = serializer.save(user=self.request.user)
		user = self.request.user
		user.current_cv = cv
		user.save()

class CvDetailView(generics.RetrieveAPIView):
	serializer_class = CvSerializer

	def get_object(self):
		user = self.request.user
		cv = user.current_cv

		if not cv:
			cv = Cv.objects.filter(user=user).first()
			if not cv:
				cv = Cv.objects.create(user=user)
				user.current_cv = cv
				user.save()
		return cv

class CvListView(generics.ListAPIView):
	serializer_class = CvSerializer

	def get_queryset(self):
		user = self.request.user
		return Cv.objects.filter(user=user)

class CvDeleteView(generics.DestroyAPIView):
	serializer_class = CvSerializer
	lookup_field = 'id'

	def get_queryset(self):
		user = self.request.user
		return Cv.objects.filter(user=user)