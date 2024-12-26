from django.db import models

class AreaInteresse(models.Model):
  ID = models.AutoField(primary_key=True)
  nome = models.CharField(max_length=150)

  def __str__(self):
    return self.nome