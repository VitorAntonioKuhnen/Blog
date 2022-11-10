from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User   

def logar(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        check = auth.authenticate(request, username=usuario, password=senha)
        
        if check is not None:
            auth.login(request, check)
            print(check)
            return redirect('index')
        else:
            messages.error(request, 'Usuario ou Senha Incorretos!!')
            return redirect('logar')
    else:        
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('logar')


def cadastro(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        senha_2 = request.POST.get('senha_2')
        if len(usuario)>= 3:
            if senha == senha_2:
                if len(senha) >= 5 and len(senha) <= 12:
                    User.objects.create_user(username=usuario, password=senha)
                    return redirect('logar')
                else:
                    messages.error(request, 'Senha é menor que 5 ou maior que 12 caracteres!!') 
                    return redirect('cadastro')
            else:
                messages.error(request, 'Senha informadas são diferentes!!') 
                return redirect('cadastro')
        else:
            messages.error(request, 'Usuario informado é menor que 3 caracters!!')
            return redirect('cadastro')   
    else:
        return render(request, 'cadastro.html')    