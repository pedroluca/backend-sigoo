from rest_framework import serializers
from .models import Usuario
from area_interesse.models import AreaInteresse

class UsuarioSerializer(serializers.ModelSerializer):
  area_interesse = serializers.PrimaryKeyRelatedField(queryset=AreaInteresse.objects.all(), many=True)
  
  class Meta:
    model = Usuario
    fields = '__all__'