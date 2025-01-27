from rest_framework import serializers
from .models import Usuario
from area_interesse.models import AreaInteresse

class UsuarioSerializer(serializers.ModelSerializer):
    area_interesse = serializers.PrimaryKeyRelatedField(queryset=AreaInteresse.objects.all(), many=True)
    password = serializers.CharField(write_only=True)
  
    class Meta:
        model = Usuario
        fields = '__all__'

    def validate_username(self, value):
        if Usuario.objects.filter(username=value).exists():
            raise serializers.ValidationError('Já existe um usuário com este username.')
        return value

    def validate_email(self, value):
        if Usuario.objects.filter(email=value).exists():
            raise serializers.ValidationError('Já existe um usuário com este email.')
        return value

    def validate_matricula(self, value):
        if Usuario.objects.filter(matricula=value).exists():
            raise serializers.ValidationError('Já existe um usuário com esta matrícula.')
        return value

    def create(self, validated_data):
        user = Usuario.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            nome=validated_data.get('nome', ''),
            matricula=validated_data.get('matricula', ''),
            Usuario_TIPO=validated_data['Usuario_TIPO'],
            quantidade_orientandos=validated_data.get('quantidade_orientandos', 0),
            tema=validated_data.get('tema', ''),
        )
        user.area_interesse.set(validated_data.get('area_interesse', []))
        return user

class UsuarioUpdateSerializer(serializers.ModelSerializer):
    area_interesse = serializers.PrimaryKeyRelatedField(queryset=AreaInteresse.objects.all(), many=True, required=False)
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Usuario
        fields = '__all__'

        def update(self, instance, validated_data):
            if 'username' in validated_data:
                instance.username = validated_data.get('username', instance.username)
            if 'email' in validated_data:
                instance.email = validated_data.get('email', instance.email)
            if 'nome' in validated_data:
                instance.nome = validated_data.get('nome', instance.nome)
            if 'matricula' in validated_data:
                instance.matricula = validated_data.get('matricula', instance.matricula)
            if 'Usuario_TIPO' in validated_data:
                instance.Usuario_TIPO = validated_data.get('Usuario_TIPO', instance.Usuario_TIPO)
            if 'area_interesse' in validated_data:
                instance.area_interesse.set(validated_data['area_interesse'])
            if 'quantidade_orientandos' in validated_data:
                instance.quantidade_orientandos = validated_data.get('quantidade_orientandos', instance.quantidade_orientandos)
            if 'tema' in validated_data:
                instance.tema = validated_data.get('tema', instance.tema)
            instance.save()
            return instance
        
class PasswordUpdateSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)

    def validate_new_password(self, value):
        if self.instance.check_password(value):
            raise serializers.ValidationError("A nova senha não pode ser igual à senha anterior.")
        return value

    def update(self, instance, validated_data):
        if not instance.check_password(validated_data['old_password']):
            raise serializers.ValidationError({"old_password": "Senha antiga incorreta."})
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance