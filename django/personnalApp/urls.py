from django.urls import path
from .views import PersonnalGetView

urlpatterns = [
	path('get/', PersonnalGetView.as_view(), name='personnal-get'),
]