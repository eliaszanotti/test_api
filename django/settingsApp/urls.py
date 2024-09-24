from django.urls import path
from .views import SettingsGetView, SettingsUpdateView, ColorSchemeGetView

urlpatterns = [
    path('get/', SettingsGetView.as_view(), name='settings-get'),
    path('update/', SettingsUpdateView.as_view(), name='settings-update'),
	path('color_scheme/<str:id>/', ColorSchemeGetView.as_view(), name='color-scheme-get'),
]
