from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Orientacao
from .serializers import OrientacaoSerializer

class OrientacaoList(generics.ListCreateAPIView):
  queryset = Orientacao.objects.all()
  serializer_class = OrientacaoSerializer
  permission_classes = [IsAuthenticated]

class OrientacaoCreate(generics.CreateAPIView):
  queryset = Orientacao.objects.all()
  serializer_class = OrientacaoSerializer
  lookup_field = 'pk'
  permission_classes = [IsAuthenticated]

class OrientacaoDetail(generics.RetrieveAPIView):
  queryset = Orientacao.objects.all()
  serializer_class = OrientacaoSerializer
  lookup_field = 'pk'
  permission_classes = [IsAuthenticated]

class OrientacaoUpdate(generics.UpdateAPIView):
  queryset = Orientacao.objects.all()
  serializer_class = OrientacaoSerializer
  lookup_field = 'pk'
  permission_classes = [IsAuthenticated]

class OrientacaoDelete(generics.DestroyAPIView):
  queryset = Orientacao.objects.all()
  serializer_class = OrientacaoSerializer
  lookup_field = 'pk'
  permission_classes = [IsAuthenticated]