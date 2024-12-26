from rest_framework import serializers
from .models import AreaInteresse

class AreaInteresseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaInteresse
        fields = '__all__'