from django.urls import path
from .views import HobbieListView, HobbieCreateView, HobbieUpdateView, HobbieDeleteView

urlpatterns = [
    path('list/', HobbieListView.as_view(), name='hobbie-list'),
    path('create/', HobbieCreateView.as_view(), name='hobbie-create'),
    path('update/<int:id>/', HobbieUpdateView.as_view(), name='hobbie-update'),
    path('delete/<int:id>/', HobbieDeleteView.as_view(), name='hobbie-delete'),
]
