from rest_framework import serializers, generics
from .models import Experience
from django.contrib.auth import get_user_model

User = get_user_model()

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        exclude = ['cv']

class ExperienceListView(generics.ListAPIView):
    serializer_class = ExperienceSerializer

    def get_queryset(self):
        user = self.request.user
        cv = user.current_cv
        return Experience.objects.filter(cv=cv)

class ExperienceCreateView(generics.CreateAPIView):
    serializer_class = ExperienceSerializer

    def perform_create(self, serializer):
        cv = self.request.user.current_cv
        Experience.objects.create(cv=cv)

class ExperienceUpdateView(generics.UpdateAPIView):
    serializer_class = ExperienceSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        cv = user.current_cv
        queryset = Experience.objects.filter(cv=cv)
        experience_id = self.kwargs.get('id')
        if not queryset.filter(id=experience_id).exists():
            raise serializers.ValidationError("This experience is not part of your CV.")
        return queryset

class ExperienceDeleteView(generics.DestroyAPIView):
    serializer_class = ExperienceSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        cv = user.current_cv
        return Experience.objects.filter(cv=cv)
