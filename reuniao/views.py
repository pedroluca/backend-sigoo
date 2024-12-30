from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Reuniao
from .serializers import ReuniaoSerializer
from api_rest.permissions import IsTipo1

class ReuniaoList(generics.ListCreateAPIView):
  queryset = Reuniao.objects.all()
  serializer_class = ReuniaoSerializer
  permission_classes = [IsAuthenticated]

class ReuniaoCreate(generics.CreateAPIView):
  queryset = Reuniao.objects.all()
  serializer_class = ReuniaoSerializer
  lookup_field = 'pk'
  permission_classes = [IsAuthenticated, IsTipo1]

class ReuniaoDetail(generics.RetrieveAPIView):
  queryset = Reuniao.objects.all()
  serializer_class = ReuniaoSerializer
  lookup_field = 'pk'
  permission_classes = [IsAuthenticated]

class ReuniaoUpdate(generics.UpdateAPIView):
  queryset = Reuniao.objects.all()
  serializer_class = ReuniaoSerializer
  lookup_field = 'pk'
  permission_classes = [IsAuthenticated, IsTipo1]

class ReuniaoDelete(generics.DestroyAPIView):
  queryset = Reuniao.objects.all()
  serializer_class = ReuniaoSerializer
  lookup_field = 'pk'
  permission_classes = [IsAuthenticated, IsTipo1]