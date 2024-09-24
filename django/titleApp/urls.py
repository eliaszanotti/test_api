from django.urls import path
from .views import TitleGetView, TitleUpdateView

urlpatterns = [
    path('get/', TitleGetView.as_view(), name='title-get'),
    path('update/', TitleUpdateView.as_view(), name='title-update'),
]