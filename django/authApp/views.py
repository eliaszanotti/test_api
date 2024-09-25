from rest_framework import generics, serializers, status
from .models import CustomUser
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response

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

class CustomTokenObtainPairView(TokenObtainPairView):
	def post(self, request, *args, **kwargs):
		response = super().post(request, *args, **kwargs)
		if response.status_code == status.HTTP_200_OK:
			refresh_token = response.data['refresh']
			response.set_cookie(
				key='refresh_token',
				value=refresh_token,
				httponly=True,
				secure=True,
				samesite='Strict',
			)
			del response.data['refresh']
		return response


class CustomTokenRefreshView(TokenRefreshView):
	def post(self, request, *args, **kwargs):
		refresh_token = request.COOKIES.get('refresh_token')
		if refresh_token is None:
			return Response({'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)
		request.data['refresh'] = refresh_token
		return super().post(request, *args, **kwargs)

class RegisterView(generics.CreateAPIView):
	queryset = CustomUser.objects.all()
	permission_classes = AllowAny
	serializer_class = UserSerializer

class LogoutView(generics.GenericAPIView):
	def post(self, request, *args, **kwargs):
		response = Response(status=status.HTTP_200_OK)
		response.delete_cookie('refresh_token')
		return response