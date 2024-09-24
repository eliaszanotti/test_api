from django.urls import path
from .views import LangListView, LangCreateView, LangUpdateView, LangDeleteView

urlpatterns = [
    path('list/', LangListView.as_view(), name='lang-list'),
    path('create/', LangCreateView.as_view(), name='lang-create'),
    path('update/<int:id>/', LangUpdateView.as_view(), name='lang-update'),
    path('delete/<int:id>/', LangDeleteView.as_view(), name='lang-delete'),
]