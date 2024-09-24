from rest_framework import serializers, generics, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from cvApp.models import Cv

User = get_user_model()

class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['cv']

class BaseListView(generics.ListAPIView):
    """
    This view returns a list of objects filtered by the current user's CV.
    """
    def get_queryset(self):
        user = self.request.user
        cv = user.current_cv
        return self.model.objects.filter(cv=cv)

class BaseCreateView(generics.CreateAPIView):
    """
    This view creates a new object and associates it with the current user's CV.
    """
    def perform_create(self, serializer):
        cv = self.request.user.current_cv
        serializer.save(cv=cv)

class BaseUpdateView(generics.UpdateAPIView):
    """
    This view updates an existing object if it is part of the current user's CV.
    """
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
    """
    This view deletes an existing object if it is part of the current user's CV.
    """
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        cv = user.current_cv
        return self.model.objects.filter(cv=cv)

class BaseGetView(generics.GenericAPIView):
    """
    This view retrieves an object associated with the current user's CV or creates one if it doesn't exist.
    """
    def get(self, request, *args, **kwargs):
        user = request.user
        cv = user.current_cv

        if not cv:
            cv = Cv.objects.filter(user=user).first()
            if not cv:
                cv = Cv.objects.create(user=user)
                user.current_cv = cv
                user.save()

        instance, created = self.model.objects.get_or_create(cv=cv)
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BaseUpdateGenericView(generics.GenericAPIView):
    """
    This view updates fields of an object associated with the current user's CV.
    """
    def put(self, request, *args, **kwargs):
        user = self.request.user
        cv = user.current_cv
        if not cv:
            return Response({"error": "No current CV found."}, status=status.HTTP_400_BAD_REQUEST)

        instance, created = self.model.objects.get_or_create(cv=cv)
        updated = False
        for field, value in request.data.items():
            if hasattr(instance, field):
                setattr(instance, field, value)
                updated = True

        if updated:
            instance.save()
            return Response({"success": "Fields updated successfully."}, status=status.HTTP_200_OK)
        return Response({"error": "No valid fields provided."}, status=status.HTTP_400_BAD_REQUEST)
