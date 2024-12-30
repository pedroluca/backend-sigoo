from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import AreaInteresse
from .serializers import AreaInteresseSerializer

class AreaInteresseList(generics.ListCreateAPIView):
  queryset = AreaInteresse.objects.all()
  serializer_class = AreaInteresseSerializer
  permission_classes = [AllowAny]

class AreaInteresseCreate(generics.CreateAPIView):
  queryset = AreaInteresse.objects.all()
  serializer_class = AreaInteresseSerializer
  lookup_field = 'pk'
  permission_classes = [IsAdminUser]

class AreaInteresseDetail(generics.RetrieveAPIView):
  queryset = AreaInteresse.objects.all()
  serializer_class = AreaInteresseSerializer
  lookup_field = 'pk'

class AreaInteresseUpdate(generics.UpdateAPIView):
  queryset = AreaInteresse.objects.all()
  serializer_class = AreaInteresseSerializer
  lookup_field = 'pk'
  permission_classes = [IsAdminUser]

class AreaInteresseDelete(generics.DestroyAPIView):
  queryset = AreaInteresse.objects.all()
  serializer_class = AreaInteresseSerializer
  lookup_field = 'pk'
  permission_classes = [IsAdminUser]