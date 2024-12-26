from django.db import models

class Usuario(models.Model):
  ID = models.AutoField(primary_key=True)
  nome = models.CharField(max_length=150, default='')
  email = models.CharField(max_length=150, default='')
  usuario = models.CharField(max_length=50, default='')
  senha = models.CharField(max_length=150, default='')
  matricula = models.CharField(max_length=20, default='')
  Usuario_TIPO = models.IntegerField()
  area_interesse = models.ManyToManyField('area_interesse.AreaInteresse')