from django.shortcuts import render
from rest_framework import generics
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioList(generics.ListCreateAPIView):
  queryset = Usuario.objects.all()
  serializer_class = UsuarioSerializer

class UsuarioCreate(generics.CreateAPIView):
  queryset = Usuario.objects.all()
  serializer_class = UsuarioSerializer
  lookup_field = 'pk'

class UsuarioDetail(generics.RetrieveAPIView):
  queryset = Usuario.objects.all()
  serializer_class = UsuarioSerializer
  lookup_field = 'pk'

class UsuarioUpdate(generics.UpdateAPIView):
  queryset = Usuario.objects.all()
  serializer_class = UsuarioSerializer
  lookup_field = 'pk'

class UsuarioDelete(generics.DestroyAPIView):
  queryset = Usuario.objects.all()
  serializer_class = UsuarioSerializer
  lookup_field = 'pk'