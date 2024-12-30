from django.db import models

class Atividade(models.Model):
  ID = models.AutoField(primary_key=True)
  descricao = models.CharField(max_length=300, default='')
  foiFeita = models.BooleanField(default=False)
  prazo = models.DateField()
  fk_Orientacao_ID = models.ForeignKey('orientacao.Orientacao', on_delete=models.CASCADE)