from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Usuario
from .serializers import UsuarioSerializer, UsuarioUpdateSerializer
from orientacao.models import Orientacao

class ValidUser(APIView):
    def get(self, request):
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data)

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
                quantidade_orientandos=serializer.validated_data.get('quantidade_orientandos', 0),
            )
            user.area_interesse.set(serializer.validated_data.get('area_interesse', []))
            return Response({'message': 'Usuário criado com sucesso!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioDetail(generics.RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    lookup_field = 'pk'

class UsuarioUpdate(generics.UpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioUpdateSerializer
    lookup_field = 'pk'

class UsuarioDelete(generics.DestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    lookup_field = 'pk'

class GetAlunoOrientacao(APIView):
    def get(self, request, id_aluno):
        try:
            orientacao = Orientacao.objects.get(fk_Usuario_ID_Aluno=id_aluno)
            return Response({
                'orientacao_id': orientacao.ID,
                'professor_id': orientacao.fk_Usuario_ID_Professor.ID
            }, status=status.HTTP_200_OK)
        except Orientacao.DoesNotExist:
            return Response({'error': 'Orientação não encontrada'}, status=status.HTTP_404_NOT_FOUND)

class GetProfessorOrientacoes(APIView):
    def get(self, request):
        orientacoes = Orientacao.objects.filter(fk_Usuario_ID_Professor=request.user.ID).values_list('ID', flat=True)
        return Response({'orientacoes_ids': list(orientacoes)}, status=status.HTTP_200_OK)