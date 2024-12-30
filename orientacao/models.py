from django.db import models

class Orientacao(models.Model):
  ID = models.AutoField(primary_key=True)
  fk_Usuario_ID_Aluno = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE, related_name='orientacao_aluno')
  fk_Usuario_ID_Professor = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE, related_name='orientacao_professor')
  solicitacaoAceita = models.BooleanField(default=False)