from django.shortcuts import render
from rest_framework import generics
from .models import AreaInteresse
from .serializers import AreaInteresseSerializer

class AreaInteresseList(generics.ListCreateAPIView):
  queryset = AreaInteresse.objects.all()
  serializer_class = AreaInteresseSerializer

class AreaInteresseCreate(generics.CreateAPIView):
  queryset = AreaInteresse.objects.all()
  serializer_class = AreaInteresseSerializer
  lookup_field = 'pk'

class AreaInteresseDetail(generics.RetrieveAPIView):
  queryset = AreaInteresse.objects.all()
  serializer_class = AreaInteresseSerializer
  lookup_field = 'pk'

class AreaInteresseUpdate(generics.UpdateAPIView):
  queryset = AreaInteresse.objects.all()
  serializer_class = AreaInteresseSerializer
  lookup_field = 'pk'

class AreaInteresseDelete(generics.DestroyAPIView):
  queryset = AreaInteresse.objects.all()
  serializer_class = AreaInteresseSerializer
  lookup_field = 'pk'