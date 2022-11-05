from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .models import Categoria
from django.contrib.auth.models import User

from blog.models import Publicacao


def inicio(request):
    return render(request)


def cadastroPub(request):
    return render(request, 'CadPubli.html')


def publicacao(request):
    return render(request, 'publicacao.html')


def criaPub(request):
    contexto = {"categorias": Categoria.objects.all()}


    if request.method == "POST":
        titulo = request.POST.get('titulo')
        resumo = request.POST.get('resumo')
        conteudo = request.POST.get('conteudo')
        # imagem = Publicacao.objects.all()
        imagem = request.FILES.get('imagem')
        idCategoria = Categoria.objects.get(id=request.POST.get('tipCateg'))
    

        if titulo is NULL:
            messages.error(request, "Informe um Titulo!")

        elif resumo is NULL:
            messages.error(request, "Adicione um Resumo")

        elif conteudo is NULL:
            messages.error(
                request, "É necessario adicionar o conteudo para criar uma publicação")

        else:
            print("Titulo: " + titulo)
            print("Resumo:" + resumo)
            print("Conteudo:" + conteudo)
            print(imagem)
            # print(categoria)

            Publicacao.objects.create(titulo=titulo, resumo=resumo, conteudo=conteudo, endImage=imagem, visualizacoes=0, usuario_id=request.user.id, categoria=idCategoria)
            return redirect('publicacao')

    else:
    #     print("Titulo:" + titulo)
    #     print("Resumo:" + resumo)
    #     print("Conteudo:" + conteudo)
    #     print("Imagem:" + imagem)
    #     print("Categoria:" + categoria)
        return render(request, 'CadPubli.html', contexto)
