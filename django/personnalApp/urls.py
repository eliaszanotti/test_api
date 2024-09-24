from django.urls import path
from .views import PersonnalGetView, PersonnalUpdateView

urlpatterns = [
	path('get/', PersonnalGetView.as_view(), name='personnal-get'),
	path('update/', PersonnalUpdateView.as_view(), name='personnal-update'),
]