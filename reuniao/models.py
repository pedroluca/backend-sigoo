from django.db import models

class Reuniao(models.Model):
  ID = models.AutoField(primary_key=True)
  titulo = models.CharField(max_length=45)
  data_agendada = models.DateField()
  horario_agendado = models.TimeField()
  justificativa = models.CharField(max_length=100, blank=True, null=True)
  foiJustificada = models.BooleanField(default=False)
  foiFeita = models.BooleanField(default=False)
  fk_Orientacao_ID = models.ForeignKey('orientacao.Orientacao', on_delete=models.CASCADE)