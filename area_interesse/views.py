from rest_framework import generics
from rest_framework.permissions import AllowAny
from api_rest.permissions import IsTipo1
from .models import AreaInteresse
from .serializers import AreaInteresseSerializer
from django.http import JsonResponse
from django.views import View

class AreaInteresseList(generics.ListCreateAPIView):
  queryset = AreaInteresse.objects.all()
  serializer_class = AreaInteresseSerializer
  permission_classes = [AllowAny]

class AreaInteresseCreate(generics.CreateAPIView):
  queryset = AreaInteresse.objects.all()
  serializer_class = AreaInteresseSerializer
  lookup_field = 'pk'
  permission_classes = [AllowAny]

  def perform_create(self, serializer):
    print("Dados recebidos:", self.request.data)  # Para debug
    serializer.save()

class AreaInteresseDetail(generics.RetrieveAPIView):
  queryset = AreaInteresse.objects.all()
  serializer_class = AreaInteresseSerializer
  lookup_field = 'pk'

class AreaInteresseUpdate(generics.UpdateAPIView):
  queryset = AreaInteresse.objects.all()
  serializer_class = AreaInteresseSerializer
  lookup_field = 'pk'
  permission_classes = [IsTipo1]

class AreaInteresseDelete(generics.DestroyAPIView):
  queryset = AreaInteresse.objects.all()
  serializer_class = AreaInteresseSerializer
  lookup_field = 'pk'
  permission_classes = [IsTipo1]

class AdicionarAreasView(View):
  def get(self, request):
    areas = [
      'Teste de software', 'Redes de Computadores', 'Agricultura Digital',
      'Algoritmos', 'Análise e Projeto de Sistemas', 'Aprendizado de Máquina',
      'Avaliação de Desempenho de Sistemas', 'Banco de Dados', 'Desenvolvimento para Dispositivos Móveis',
      'Desenvolvimento Multiplataforma', 'Desenvolvimento Web', 'DevOps', 'E-Learning',
      'Engenharia de Software', 'Estatística', 'Estrutura de Dados', 'Gestão de Tecnologia da Informação',
      'Inclusão Digital'
    ]

    adicionadas = 0
    for nome in areas:
      if not AreaInteresse.objects.filter(nome=nome).exists():  # Evita duplicação
        AreaInteresse.objects.create(nome=nome)
        adicionadas += 1

    return JsonResponse({'mensagem': f'{adicionadas} áreas adicionadas!'}, status=200)
