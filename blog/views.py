from django.shortcuts import render, redirect


def inicio(request):
    return render(request)

def cadastroPub(request):
    return render(request, 'CadPubli.html') 

def publicacao(request):
    return render(request, 'publicacao.html')    
