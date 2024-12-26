from django.db import models

class Post(models.Model):
  ID = models.AutoField(primary_key=True)
  ID_autor = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)
  titulo = models.CharField(max_length=100)
  conteudo = models.TextField()
  caminho_arquivo = models.CharField(max_length=100)
  data_publicacao = models.DateField(auto_now_add=True)
  horario_publicacao = models.CharField(max_length=10)
  fk_Orientacao_ID = models.ForeignKey('orientacao.Orientacao', on_delete=models.CASCADE)