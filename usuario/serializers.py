from rest_framework import serializers
from .models import Usuario
from area_interesse.models import AreaInteresse

class UsuarioSerializer(serializers.ModelSerializer):
  area_interesse = serializers.PrimaryKeyRelatedField(queryset=AreaInteresse.objects.all(), many=True)
  password = serializers.CharField(write_only=True)

  class Meta:
      model = Usuario
      fields = '__all__'

  def create(self, validated_data):
      user = Usuario.objects.create_user(
          username=validated_data['username'],
          email=validated_data.get('email', ''),
          password=validated_data['password'],
          nome=validated_data.get('nome', ''),
          matricula=validated_data.get('matricula', ''),
          Usuario_TIPO=validated_data['Usuario_TIPO'],
          quantidade_orientandos=validated_data.get('quantidade_orientandos', 0),
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
      if 'password' in validated_data:
          instance.set_password(validated_data['password'])
      if 'area_interesse' in validated_data:
          instance.area_interesse.set(validated_data['area_interesse'])
      if 'quantidade_orientandos' in validated_data:
          instance.quantidade_orientandos = validated_data.get('quantidade_orientandos', instance.quantidade_orientandos)
      instance.save()
      return instance