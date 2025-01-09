from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Orientacao
from .serializers import OrientacaoSerializer, OrientacaoCreateWithEmailsSerializer
from api_rest.permissions import IsTipo1

class OrientacaoList(generics.ListCreateAPIView):
  queryset = Orientacao.objects.all()
  serializer_class = OrientacaoSerializer

class OrientacaoCreate(generics.CreateAPIView):
  queryset = Orientacao.objects.all()
  serializer_class = OrientacaoSerializer
  lookup_field = 'pk'

class OrientacaoDetail(generics.RetrieveAPIView):
  queryset = Orientacao.objects.all()
  serializer_class = OrientacaoSerializer
  lookup_field = 'pk'

class OrientacaoUpdate(generics.UpdateAPIView):
  queryset = Orientacao.objects.all()
  serializer_class = OrientacaoSerializer
  lookup_field = 'pk'
  permission_classes = [IsAuthenticated, IsTipo1]

class OrientacaoDelete(generics.DestroyAPIView):
  queryset = Orientacao.objects.all()
  serializer_class = OrientacaoSerializer
  lookup_field = 'pk'
  permission_classes = [IsAuthenticated, IsTipo1]

class OrientacaoCreateWithEmails(APIView):
  permission_classes = [IsAuthenticated]

  def post(self, request):
      serializer = OrientacaoCreateWithEmailsSerializer(data=request.data)
      if serializer.is_valid():
          orientacao = serializer.save()
          return Response(OrientacaoSerializer(orientacao).data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)