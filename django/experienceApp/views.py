from commonApp.views import BaseModelSerializer, BaseListView, BaseCreateView, BaseUpdateView, BaseDeleteView
from .models import Experience

class ExperienceSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Experience

class ExperienceListView(BaseListView):
    serializer_class = ExperienceSerializer
    model = Experience

class ExperienceCreateView(BaseCreateView):
    serializer_class = ExperienceSerializer
    model = Experience

class ExperienceUpdateView(BaseUpdateView):
    serializer_class = ExperienceSerializer
    model = Experience

class ExperienceDeleteView(BaseDeleteView):
    serializer_class = ExperienceSerializer
    model = Experience
