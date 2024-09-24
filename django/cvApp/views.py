from rest_framework import serializers, generics, permissions
from .models import Cv

class CvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cv
        fields = '__all__'

class CvCreateView(generics.CreateAPIView):
    serializer_class = CvSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CvDetailView(generics.RetrieveAPIView):
    serializer_class = CvSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return Cv.objects.get(user=self.request.user)