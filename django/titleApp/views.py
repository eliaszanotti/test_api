from commonApp.views import BaseGetView, BaseUpdateGenericView
from .models import Title
from rest_framework import serializers

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'

class TitleGetView(BaseGetView):
    serializer_class = TitleSerializer
    model = Title

class TitleUpdateView(BaseUpdateGenericView):
    serializer_class = TitleSerializer
    model = Title
