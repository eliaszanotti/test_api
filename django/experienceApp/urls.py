from django.urls import path
from .views import ExperienceListView, ExperienceCreateView, ExperienceUpdateView, ExperienceDeleteView

urlpatterns = [
    path('list/', ExperienceListView.as_view(), name='experience-list'),
    path('create/', ExperienceCreateView.as_view(), name='experience-create'),
    path('update/<int:id>/', ExperienceUpdateView.as_view(), name='experience-update'),
    path('delete/<int:id>/', ExperienceDeleteView.as_view(), name='experience-delete'),
]
