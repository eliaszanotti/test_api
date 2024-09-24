from rest_framework import generics, serializers
from .models import CustomUser
from rest_framework.permissions import AllowAny

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ('username', 'password', 'email', 'current_cv')
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		user = CustomUser.objects.create_user(
			username=validated_data['username'],
			password=validated_data['password'],
			email=validated_data['email'],
			current_cv=validated_data['current_cv']
		)
		return user

class RegisterView(generics.CreateAPIView):
	queryset = CustomUser.objects.all()
	permission_classes = AllowAny
	serializer_class = UserSerializer