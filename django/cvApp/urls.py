from django.urls import path
from .views import CvCreateView, CvDetailView, CvListView, CvDeleteView

urlpatterns = [
    path('create/', CvCreateView.as_view(), name='cv-create'),
    path('detail/', CvDetailView.as_view(), name='cv-detail'),
	path('list/', CvListView.as_view(), name='cv-list'),
	path('delete/<int:id>/', CvDeleteView.as_view(), name='cv-delete'),
]