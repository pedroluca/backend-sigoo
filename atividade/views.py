from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Atividade
from .serializers import AtividadeSerializer
from api_rest.permissions import IsTipo1

class AtividadeList(generics.ListCreateAPIView):
  queryset = Atividade.objects.all()
  serializer_class = AtividadeSerializer
  permission_classes = [IsAuthenticated]

class AtividadeCreate(generics.CreateAPIView):
  queryset = Atividade.objects.all()
  serializer_class = AtividadeSerializer
  lookup_field = 'pk'
  permission_classes = [IsAuthenticated, IsTipo1]

class AtividadeDetail(generics.RetrieveAPIView):
  queryset = Atividade.objects.all()
  serializer_class = AtividadeSerializer
  lookup_field = 'pk'
  permission_classes = [IsAuthenticated]

class AtividadeUpdate(generics.UpdateAPIView):
  queryset = Atividade.objects.all()
  serializer_class = AtividadeSerializer
  lookup_field = 'pk'
  permission_classes = [IsAuthenticated]

class AtividadeDelete(generics.DestroyAPIView):
  queryset = Atividade.objects.all()
  serializer_class = AtividadeSerializer
  lookup_field = 'pk'
  permission_classes = [IsAuthenticated, IsTipo1]