from commonApp.views import BaseModelSerializer, BaseListView, BaseCreateView, BaseUpdateView, BaseDeleteView
from .models import Lang

class LangSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Lang

class LangListView(BaseListView):
    serializer_class = LangSerializer
    model = Lang

class LangCreateView(BaseCreateView):
    serializer_class = LangSerializer
    model = Lang

class LangUpdateView(BaseUpdateView):
    serializer_class = LangSerializer
    model = Lang

class LangDeleteView(BaseDeleteView):
    serializer_class = LangSerializer
    model = Lang