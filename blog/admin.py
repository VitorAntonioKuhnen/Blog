from re import search
from django.contrib import admin
from .models import *

class PublicacaoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'resumo', 'visualizacoes']
    list_display_links = ['titulo']
    search_fields = ['titulo', 'resumo', 'conteudo']

admin.site.register(Publicacao, PublicacaoAdmin)

class ComentariosAdmin(admin.ModelAdmin):
    list_display = ['comentario', 'usuario', 'datHora']
    list_display_links = ['comentario', 'usuario', 'datHora']
    search_fields = ['comentario', 'usuario']

admin.site.register(Comentarios, ComentariosAdmin)    

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nmCategoria']
    list_display_links = ['nmCategoria']
    search_fields = ['nmCategoria']

admin.site.register(Categoria, CategoriaAdmin)