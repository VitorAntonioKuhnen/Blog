from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from django.contrib import auth, messages

from blog.models import Publicacao


def inicio(request):
    return render(request)

def cadastroPub(request):
    return render(request, 'CadPubli.html') 

def publicacao(request):
    return render(request, 'publicacao.html')   

def criaPub(request):
    titulo = request.POST.get('titulo')
    resumo = request.POST.get('resumo') 
    conteudo = request.POST.get('conteudo') 
    imagem = Publicacao.objects.all()
    imagem = request.FILE.get('imagem')
    categoria = request.POST.get('')
    

    if titulo is NULL:
        messages.error(request,"Informe um Titulo!")
        
    elif resumo is NULL:
        messages.error(request,"Adicione um Resumo")

    elif conteudo is NULL:
        messages.error(request,"É necessario adicionar o conteudo para criar uma publicação")

    else:
        Publicacao.objects.create(titulo = titulo, resumo=resumo, conteudo=conteudo, endImagem=imagem, visualizacao=0, usuario_id=request.user.id, categoria=categoria)
        return redirect(request, 'inicio')
        

    return render(request, 'publicacao.html')    
