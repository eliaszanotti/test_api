from commonApp.views import BaseModelSerializer, BaseListView, BaseCreateView, BaseUpdateView, BaseDeleteView
from .models import Hobbie

class HobbieSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Hobbie

class HobbieListView(BaseListView):
    serializer_class = HobbieSerializer
    model = Hobbie

class HobbieCreateView(BaseCreateView):
    serializer_class = HobbieSerializer
    model = Hobbie

class HobbieUpdateView(BaseUpdateView):
    serializer_class = HobbieSerializer
    model = Hobbie

class HobbieDeleteView(BaseDeleteView):
    serializer_class = HobbieSerializer
    model = Hobbie
