from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from blog.models import Categoria, Favorito, Publicacao, Comentarios, Favorito
from django.contrib.auth.models import User
from django.db.models import Q


def inicio(request):
    publicacoes = Publicacao.objects.all()
    if request.user.is_superuser:
        # Permissão para que os super usuarios possam verificar mais de um item
        favoritos = Favorito.objects.all()
        return render(request, 'inicio.html', {'publicacoes': publicacoes, 'favoritos': favoritos, "categorias": Categoria.objects.all()})
    else:
        favoritos = Favorito.objects.filter(usuario_id=request.user.id)
        return render(request, 'inicio.html', {'publicacoes': publicacoes, 'favoritos': favoritos, "categorias": Categoria.objects.all()})


def cadastroPub(request):
    return render(request, 'CadPubli.html', {"categorias": Categoria.objects.all()})


def publicacao(request, id):
    publi = Publicacao.objects.get(id=id)
    comentPubli = Comentarios.objects.filter(publicacao=id)

    if request.method == "POST":
        if request.user.is_authenticated:
            comentario = request.POST.get('cxComentario').strip()
            checkNormal = request.POST.get('check')

            if comentario == '':
                messages.error(request, "Adicione um Resumo")

            else:
                if checkNormal == '1':
                    Comentarios.objects.create(
                        comentario=comentario, usuario_id=request.user.id, publicacao_id=id)
                    return render(request, 'publicacao.html', {'publi': publi, 'comentPubli': comentPubli, 'categorias': Categoria.objects.all()})
                else:
                    Comentarios.objects.create(
                        comentario=comentario, publicacao_id=id)
                    return render(request, 'publicacao.html', {'publi': publi, 'comentPubli': comentPubli, 'categorias': Categoria.objects.all()})
        else:
            return render(request, 'publicacao.html', {'publi': publi, 'comentPubli': comentPubli, 'categorias': Categoria.objects.all()})

    else:
        publi.visualizacoes += 1
        publi.save()
        return render(request, 'publicacao.html', {'publi': publi, 'comentPubli': comentPubli, 'categorias': Categoria.objects.all()})


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

            Publicacao.objects.create(titulo=titulo, resumo=resumo, conteudo=conteudo, endImage=imagem,
                                      visualizacoes=0, usuario_id=request.user.id, categoria=idCategoria)
            return redirect('inicio')

    else:
        return render(request, 'CadPubli.html', contexto)


def favoritar(request, id):
    publi = Publicacao.objects.get(id=id)
    favoritei = Favorito.objects.filter(usuario_id=request.user.id)
    existe = True

    for favorit in favoritei:
        print(favorit.id)
        if favorit.publicacao.id == publi.id:
            existe = False  # Se caso existir alguma publicação que já foi favoritada não irá deixar adicionar mais de 1 vez
            break
        else:
            existe = True

    if existe:
        Favorito.objects.create(
            usuario_id=request.user.id, publicacao_id=publi.id)
        return redirect('inicio')
    else:
        return redirect('inicio')


def buscar(request):
    busca = request.GET.get('pesquisa')

    publicacoes = Publicacao.objects.filter(
        Q(titulo__icontains=busca) | Q(conteudo__icontains=busca))
    favoritos = Favorito.objects.filter(usuario_id=request.user.id)
    return render(request, 'inicio.html', {'publicacoes': publicacoes, 'favoritos': favoritos, 'categorias': Categoria.objects.all()})


def categoria(request, id):
    publicacoes = Publicacao.objects.filter(categoria_id=id)
    favoritos = Favorito.objects.filter(usuario_id=request.user.id)
    return render(request, 'inicio.html', {'publicacoes': publicacoes, 'favoritos': favoritos, 'categorias': Categoria.objects.all()})
