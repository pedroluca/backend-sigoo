from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioList(generics.ListCreateAPIView):
  queryset = Usuario.objects.all()
  serializer_class = UsuarioSerializer

class UsuarioCreate(APIView):
  permission_classes = [AllowAny]
  
  def post(self, request):
    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
      user = Usuario.objects.create_user(  # Use o método `create_user`
        username=serializer.validated_data['username'],
        email=serializer.validated_data.get('email', ''),
        password=serializer.validated_data['password'],
        nome=serializer.validated_data.get('nome', ''),
        matricula=serializer.validated_data.get('matricula', ''),
        Usuario_TIPO=serializer.validated_data['Usuario_TIPO'],
      )
      return Response({'message': 'Usuário criado com sucesso!'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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