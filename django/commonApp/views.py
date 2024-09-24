from rest_framework import serializers, generics
from django.contrib.auth import get_user_model

User = get_user_model()

class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['cv']

class BaseListView(generics.ListAPIView):
    def get_queryset(self):
        user = self.request.user
        cv = user.current_cv
        return self.model.objects.filter(cv=cv)

class BaseCreateView(generics.CreateAPIView):
    def perform_create(self, serializer):
        cv = self.request.user.current_cv
        serializer.save(cv=cv)

class BaseUpdateView(generics.UpdateAPIView):
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        cv = user.current_cv
        queryset = self.model.objects.filter(cv=cv)
        obj_id = self.kwargs.get('id')
        if not queryset.filter(id=obj_id).exists():
            raise serializers.ValidationError(f"This {self.model.__name__.lower()} is not part of your CV.")
        return queryset

class BaseDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        cv = user.current_cv
        return self.model.objects.filter(cv=cv)
