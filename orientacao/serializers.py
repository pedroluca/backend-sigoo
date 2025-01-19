from rest_framework import serializers
from .models import Orientacao
from usuario.models import Usuario

class OrientacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orientacao
        fields = '__all__'

class OrientacaoCreateWithEmailsSerializer(serializers.Serializer):
    email_aluno = serializers.EmailField()
    email_professor = serializers.EmailField()
    solicitacaoAceita = serializers.BooleanField(default=True)

    def create(self, validated_data):
        email_aluno = validated_data.get('email_aluno')
        email_professor = validated_data.get('email_professor')
        solicitacaoAceita = validated_data.get('solicitacaoAceita')

        try:
            aluno = Usuario.objects.get(email=email_aluno)
            professor = Usuario.objects.get(email=email_professor)
        except Usuario.DoesNotExist:
            raise serializers.ValidationError("Usuário não encontrado com o email fornecido.")

        orientacao = Orientacao.objects.create(
            fk_Usuario_ID_Aluno=aluno,
            fk_Usuario_ID_Professor=professor,
            solicitacaoAceita=solicitacaoAceita
        )
        return orientacao