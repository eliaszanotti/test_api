from django.urls import path
from .views import SettingsGetView, SettingsUpdateView

urlpatterns = [
    path('get/', SettingsGetView.as_view(), name='settings-get'),
    path('update/', SettingsUpdateView.as_view(), name='settings-update'),
]
