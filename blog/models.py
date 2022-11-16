from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nmCategoria = models.CharField(max_length=40)

    def __str__(self):
        return self.nmCategoria


class Publicacao(models.Model):
    titulo = models.CharField(max_length=255)
    endImage = models.ImageField(upload_to='Publicacao_img/%Y/%m/%d')
    resumo = models.TextField(max_length=1000)
    conteudo = models.TextField()
    visualizacoes = models.IntegerField()
    datHor = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.titulo


class Comentarios(models.Model):
    comentario = models.TextField()
    datHora = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, blank=True, null=True)
    publicacao = models.ForeignKey(Publicacao, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.comentario


class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    publicacao = models.ForeignKey(Publicacao, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.publicacao.titulo
