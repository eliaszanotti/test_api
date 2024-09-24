from rest_framework import serializers, generics
from .models import Formation
from django.contrib.auth import get_user_model

User = get_user_model()

class FormationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formation
        exclude = ['cv']

class FormationListView(generics.ListAPIView):
    serializer_class = FormationSerializer

    def get_queryset(self):
        user = self.request.user
        cv = user.current_cv
        return Formation.objects.filter(cv=cv)

class FormationCreateView(generics.CreateAPIView):
    serializer_class = FormationSerializer

    def perform_create(self, serializer):
        cv = self.request.user.current_cv
        Formation.objects.create(cv=cv)

class FormationUpdateView(generics.UpdateAPIView):
    serializer_class = FormationSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        cv = user.current_cv
        queryset = Formation.objects.filter(cv=cv)
        formation_id = self.kwargs.get('id')
        if not queryset.filter(id=formation_id).exists():
            raise serializers.ValidationError("This formation is not part of your CV.")
        return queryset

class FormationDeleteView(generics.DestroyAPIView):
    serializer_class = FormationSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        cv = user.current_cv
        return Formation.objects.filter(cv=cv)
