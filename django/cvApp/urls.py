from django.urls import path
from .views import CvCreateView, CvDetailView, CvListView

urlpatterns = [
    path('create/', CvCreateView.as_view(), name='cv-create'),
    path('detail/', CvDetailView.as_view(), name='cv-detail'),
	path('list/', CvListView.as_view(), name='cv-list'),
]