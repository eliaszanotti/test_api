from rest_framework import serializers, generics
from .models import Cv

class CvSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())

	class Meta:
		model = Cv
		fields = '__all__'

class CvCreateView(generics.CreateAPIView):
	serializer_class = CvSerializer

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class CvDetailView(generics.RetrieveAPIView):
	serializer_class = CvSerializer

	def get_object(self):
		return Cv.objects.get(user=self.request.user)