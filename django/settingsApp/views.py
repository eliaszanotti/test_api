from rest_framework.response import Response
from rest_framework import serializers, generics, status
from .models import Settings
from cvApp.models import Cv
from django.contrib.auth import get_user_model
from .schemes import SCHEMES

User = get_user_model()

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'

class SettingsGetView(generics.GenericAPIView):
    serializer_class = SettingsSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        cv = user.current_cv

        if not cv:
            cv = Cv.objects.filter(user=user).first()
            if not cv:
                cv = Cv.objects.create(user=user)
                user.current_cv = cv
                user.save()

        settings, created = Settings.objects.get_or_create(cv=cv)
        serializer = self.get_serializer(settings)
        data = serializer.data
        data['color_schemes'] = SCHEMES
        return Response(data, status=status.HTTP_200_OK)

class SettingsUpdateView(generics.GenericAPIView):
    serializer_class = SettingsSerializer

    def put(self, request, *args, **kwargs):
        user = self.request.user
        cv = user.current_cv
        if not cv:
            return Response({"error": "No current CV found."}, status=status.HTTP_400_BAD_REQUEST)

        settings, created = Settings.objects.get_or_create(cv=cv)
        updated = False
        for field, value in request.data.items():
            if hasattr(settings, field):
                setattr(settings, field, value)
                updated = True

        if updated:
            settings.save()
            return Response({"success": "Fields updated successfully."}, status=status.HTTP_200_OK)
        return Response({"error": "No valid fields provided."}, status=status.HTTP_400_BAD_REQUEST)
