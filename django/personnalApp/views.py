from rest_framework.response import Response
from rest_framework import serializers, generics, status
from .models import Personnal
from cvApp.models import Cv
from django.contrib.auth import get_user_model

User = get_user_model()

class PersonnalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Personnal
		fields = '__all__'

class PersonnalGetView(generics.GenericAPIView):
    serializer_class = PersonnalSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        cv = user.current_cv

        if not cv:
            cv = Cv.objects.filter(user=user).first()
            if not cv:
                cv = Cv.objects.create(user=user)
                user.current_cv = cv
                user.save()

        personnal, created = Personnal.objects.get_or_create(cv=cv)
        serializer = self.get_serializer(personnal)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PersonnalUpdateView(generics.GenericAPIView):
    serializer_class = PersonnalSerializer

    def put(self, request, *args, **kwargs):
        user = self.request.user
        cv = user.current_cv
        if not cv:
            return Response({"error": "No current CV found."}, status=status.HTTP_400_BAD_REQUEST)

        personnal, created = Personnal.objects.get_or_create(cv=cv)
        updated = False
        for field, value in request.data.items():
            if hasattr(personnal, field):
                setattr(personnal, field, value)
                updated = True

        if updated:
            personnal.save()
            return Response({"success": "Fields updated successfully."}, status=status.HTTP_200_OK)
        return Response({"error": "No valid fields provided."}, status=status.HTTP_400_BAD_REQUEST)