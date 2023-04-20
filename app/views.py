from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return HttpResponse("loja")

def cadastro(request):
    if request.method == "GET":
        return render(request,'cadastro.html')
    else:
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        usuario = User.object.filter(username=nome).first()
        if usuario:
            return HttpResponse(f'usuario já existe{nome}')
        
        usuario = User.object.filter(username=nome, password=senha)
        usuario.save()

        return HttpResponse(f'Usuario salvo com sucesso! {nome}')
    


def logar(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        usuario= authenticate(username=nome, password=senha)
        if usuario:
            login(request, usuario)
            return HttpResponse("usuario autenticado")
        else:
            return HttpResponse('usuario autenticado')


@login_required(login_url='/logar')

def pagina(request):
    return HttpResponse ('paginaaa')