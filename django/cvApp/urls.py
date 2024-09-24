from django.urls import path
from .views import CvCreateView, CvDetailView

urlpatterns = [
    path('create/', CvCreateView.as_view(), name='cv-create'),
    path('detail/', CvDetailView.as_view(), name='cv-detail'),
]