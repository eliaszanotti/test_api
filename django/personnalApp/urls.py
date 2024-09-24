from django.urls import path
from .views import ItemListCreateView, ItemDetailView, PersonnalGetOrCreateView

urlpatterns = [
	path('create/', ItemListCreateView.as_view(), name='item-list-create'),
	path('detail/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
	path('get/', PersonnalGetOrCreateView.as_view(), name='personnal-get'),
]