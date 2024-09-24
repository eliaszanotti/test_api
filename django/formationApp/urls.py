from django.urls import path
from .views import FormationListView, FormationCreateView, FormationUpdateView, FormationDeleteView

urlpatterns = [
    path('list/', FormationListView.as_view(), name='formation-list'),
    path('create/', FormationCreateView.as_view(), name='formation-create'),
    path('update/<int:id>/', FormationUpdateView.as_view(), name='formation-update'),
    path('delete/<int:id>/', FormationDeleteView.as_view(), name='formation-delete'),
]
