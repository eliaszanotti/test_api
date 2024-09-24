from rest_framework.response import Response
from rest_framework import serializers, generics, status
from .models import Title
from cvApp.models import Cv
from django.contrib.auth import get_user_model

User = get_user_model()

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'

class TitleGetView(generics.GenericAPIView):
    serializer_class = TitleSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        cv = user.current_cv

        if not cv:
            cv = Cv.objects.filter(user=user).first()
            if not cv:
                cv = Cv.objects.create(user=user)
                user.current_cv = cv
                user.save()

        title, created = Title.objects.get_or_create(cv=cv)
        serializer = self.get_serializer(title)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TitleUpdateView(generics.GenericAPIView):
    serializer_class = TitleSerializer

    def put(self, request, *args, **kwargs):
        user = self.request.user
        cv = user.current_cv
        if not cv:
            return Response({"error": "No current CV found."}, status=status.HTTP_400_BAD_REQUEST)

        title, created = Title.objects.get_or_create(cv=cv)
        updated = False
        for field, value in request.data.items():
            if hasattr(title, field):
                setattr(title, field, value)
                updated = True

        if updated:
            title.save()
            return Response({"success": "Fields updated successfully."}, status=status.HTTP_200_OK)
        return Response({"error": "No valid fields provided."}, status=status.HTTP_400_BAD_REQUEST)
