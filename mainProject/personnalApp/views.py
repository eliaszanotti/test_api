from django.shortcuts import render
from rest_framework import serializers, generics
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = '__all__'

class ItemListCreateView(generics.ListCreateAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer