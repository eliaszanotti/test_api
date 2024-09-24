from rest_framework import serializers, generics
from .models import Hobbie
from django.contrib.auth import get_user_model

User = get_user_model()

class HobbieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobbie
        exclude = ['cv']

class HobbieListView(generics.ListAPIView):
    serializer_class = HobbieSerializer

    def get_queryset(self):
        user = self.request.user
        cv = user.current_cv
        return Hobbie.objects.filter(cv=cv)

class HobbieCreateView(generics.CreateAPIView):
    serializer_class = HobbieSerializer

    def perform_create(self, serializer):
        cv = self.request.user.current_cv
        Hobbie.objects.create(cv=cv)

class HobbieUpdateView(generics.UpdateAPIView):
    serializer_class = HobbieSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        cv = user.current_cv
        queryset = Hobbie.objects.filter(cv=cv)
        hobbie_id = self.kwargs.get('id')
        if not queryset.filter(id=hobbie_id).exists():
            raise serializers.ValidationError("This hobbie is not part of your CV.")
        return queryset

class HobbieDeleteView(generics.DestroyAPIView):
    serializer_class = HobbieSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        cv = user.current_cv
        return Hobbie.objects.filter(cv=cv)
