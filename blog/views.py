from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from blog.models import Categoria, Favorito, Publicacao, Comentarios
from django.contrib.auth.models import User


def inicio(request):
    publicacoes = Publicacao.objects.all()
    if request.user.is_superuser:
        favoritos = Favorito.objects.all() # Permissão para que os super usuarios possam verificar mais de um item
        return render(request, 'inicio.html', {'publicacoes': publicacoes, 'favoritos': favoritos})
    else:
        favoritos = Favorito.objects.filter(usuario_id=request.user.id)
        return render(request, 'inicio.html', {'publicacoes':publicacoes, 'favoritos':favoritos})

def cadastroPub(request):
    return render(request, 'CadPubli.html')


def publicacao(request, id):
    publi = Publicacao.objects.get(id=id)
    comentPubli = Comentarios.objects.filter(publicacao=id)

    if request.method == "POST":
        comentario = request.POST.get('cxComentario').strip()
        checkNormal = request.POST.get('check')

        if comentario == '':
            messages.error(request, "Adicione um Resumo")
            
        else:
            if checkNormal == '1':
                Comentarios.objects.create(comentario=comentario, usuario_id=request.user.id, publicacao_id=id)   
                return render(request, 'publicacao.html', {'publi': publi, 'comentPubli':comentPubli, 'categorias':Categoria.objects.all()} ) 
            else:
                print("passou aqui 2")
                Comentarios.objects.create(comentario=comentario, publicacao_id=id)   
                return render(request, 'publicacao.html', {'publi': publi, 'comentPubli':comentPubli, 'categorias':Categoria.objects.all()} )     
                
    else:    
        return render(request, 'publicacao.html', {'publi': publi, 'comentPubli':comentPubli, 'categorias':Categoria.objects.all()} )


def criaPub(request):
    contexto = {"categorias": Categoria.objects.all()}


    if request.method == "POST":
        titulo = request.POST.get('titulo')
        resumo = request.POST.get('resumo')
        conteudo = request.POST.get('conteudo')
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

            Publicacao.objects.create(titulo=titulo, resumo=resumo, conteudo=conteudo, endImage=imagem, visualizacoes=0, usuario_id=request.user.id, categoria=idCategoria)
            return redirect('publicacao')

    else:
        return render(request, 'CadPubli.html', contexto)
