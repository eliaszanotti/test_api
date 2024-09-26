from commonApp.views import BaseGetView, BaseUpdateGenericView
from .models import Settings
from rest_framework import serializers, status, generics
from rest_framework.response import Response
from .schemes import SCHEMES
from commonApp.constants import SETTINGS_FONT_SIZES, SETTINGS_FONT_SIZES_CHOICES

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'

class SettingsGetView(BaseGetView):
    """
    We override the get method to add sizes from a constants file.
    """
    serializer_class = SettingsSerializer
    model = Settings

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response.data['sizes'] = SETTINGS_FONT_SIZES
        response.data['sizes_choices'] = SETTINGS_FONT_SIZES_CHOICES
        return response

class SettingsUpdateView(BaseUpdateGenericView):
    serializer_class = SettingsSerializer
    model = Settings

class ColorSchemeGetView(generics.GenericAPIView):
    """
    This function retrieves the color scheme associated with the given template ID.
    It returns the scheme if the ID is valid, otherwise it returns an error message.
    """
    def get(self, request, *args, **kwargs):
        scheme_id = kwargs.get('id')
        if scheme_id is None or not scheme_id.isdigit() or int(scheme_id) >= len(SCHEMES):
            return Response({"error": "Invalid scheme ID."}, status=status.HTTP_400_BAD_REQUEST)
        
        scheme = SCHEMES[int(scheme_id)]
        return Response(scheme, status=status.HTTP_200_OK)