from commonApp.views import BaseModelSerializer, BaseListView, BaseCreateView, BaseUpdateView, BaseDeleteView
from .models import Formation

class FormationSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Formation

class FormationListView(BaseListView):
    serializer_class = FormationSerializer
    model = Formation

class FormationCreateView(BaseCreateView):
    serializer_class = FormationSerializer
    model = Formation

class FormationUpdateView(BaseUpdateView):
    serializer_class = FormationSerializer
    model = Formation

class FormationDeleteView(BaseDeleteView):
    serializer_class = FormationSerializer
    model = Formation
