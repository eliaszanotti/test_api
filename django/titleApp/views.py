from commonApp.views import BaseGetView, BaseUpdateGenericView
from .models import Title
from rest_framework import serializers
from commonApp.constants import TITLE_TYPE_CHOICES

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'

class TitleGetView(BaseGetView):
    serializer_class = TitleSerializer
    model = Title

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response.data['type_choices'] = TITLE_TYPE_CHOICES
        return response

class TitleUpdateView(BaseUpdateGenericView):
    serializer_class = TitleSerializer
    model = Title
