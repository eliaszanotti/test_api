from django.urls import path
from .views import PersonnalGetView, PersonnalUpdateView, PersonnalPictureUpdateView

urlpatterns = [
	path('get/', PersonnalGetView.as_view(), name='personnal-get'),
	path('update/', PersonnalUpdateView.as_view(), name='personnal-update'),
	path('picture/update/', PersonnalPictureUpdateView.as_view(), name='personnal-picture-update'),
]