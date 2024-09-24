from rest_framework import serializers, generics
from .models import Lang
from django.contrib.auth import get_user_model

User = get_user_model()

class LangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lang
        exclude = ['cv']

class LangListView(generics.ListAPIView):
    serializer_class = LangSerializer

    def get_queryset(self):
        user = self.request.user
        cv = user.current_cv
        return Lang.objects.filter(cv=cv)

class LangCreateView(generics.CreateAPIView):
    serializer_class = LangSerializer

    def perform_create(self, serializer):
        cv = self.request.user.current_cv
        Lang.objects.create(cv=cv)

class LangUpdateView(generics.UpdateAPIView):
    serializer_class = LangSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        cv = user.current_cv
        return Lang.objects.filter(cv=cv)

class LangDeleteView(generics.DestroyAPIView):
    serializer_class = LangSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        cv = user.current_cv
        return Lang.objects.filter(cv=cv)