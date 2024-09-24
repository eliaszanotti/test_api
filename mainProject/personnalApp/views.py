from django.shortcuts import render
from rest_framework import serializers, generics
from .models import Personnal

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Personnal
		fields = '__all__'

class ItemListCreateView(generics.ListCreateAPIView):
	queryset = Personnal.objects.all()
	serializer_class = ItemSerializer

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Personnal.objects.all()
	serializer_class = ItemSerializer