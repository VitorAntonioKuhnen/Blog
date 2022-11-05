from django.db import models
from django.contrib.auth.models import User




class Categoria(models.Model):
    nmCategoria = models.CharField(max_length=40)

    def __str__(self):
        return self.nmCategoria

class Publicacao(models.Model):
    titulo = models.CharField(max_length=255)
    endImage = models.ImageField()
    resumo = models.TextField(max_length=1000)
    conteudo = models.TextField()
    visualizacoes = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.titulo

class Comentarios(models.Model):
    comentario = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    publicacao = models.ForeignKey(Publicacao, on_delete=models.DO_NOTHING)
    datHora = models.DateTimeField()
    
    def __str__(self):
        return self.comentario
