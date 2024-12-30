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
    )
    return user