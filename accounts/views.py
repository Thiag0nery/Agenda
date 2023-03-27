from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    user = auth.authenticate(request, username=usuario,password=senha)
    if not user:
        messages.error(request, 'usuario ou senha incoretos')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login com sucesso!')
        return redirect('dashboard')

def logout(request):
    return render(request, 'accounts/logout.html')
def cadastro(request):
    if request.method != 'POST':
        #messages.info(request,'Nada postado ')
        return render(request, 'accounts/cadastro.html')
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    usuario = request.POST.get('usuario')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senharepete = request.POST.get('senharepete')

    if not nome or not usuario or not sobrenome or not email or not senha or not senharepete:
        messages.error(request, "Todos os campos precisam ser preencidos ")
        return render(request, 'accounts/cadastro.html')
    try:
        validate_email(email)
    except:
        messages.error(request, "Email invalido ")
        return render(request, 'accounts/cadastro.html')
    if len(usuario) < 6:
        messages.error(request, "O usuario precisa ter 6 ou mais caracteres ")
        return render(request, 'accounts/cadastro.html')
    if len(senha) < 6:
        messages.error(request, "A senha precisa ter 6 ou mais caracteres")
        return render(request, 'accounts/cadastro.html')
    if senha != senharepete:
        messages.error(request, "As senha precisam ser iguais")
        return render(request, 'accounts/cadastro.html')
    if User.objects.filter(username=usuario).exists():
        messages.error(request, "O usuario ja existe")
        return render(request, 'accounts/cadastro.html')
    if User.objects.filter(email=email).exists():
        messages.error(request, "O email ja existe")
        return render(request, 'accounts/cadastro.html')
    print(nome)


    messages.success(request, 'Cadastrado com susseco ')

    user = User.objects.create_user(username=usuario,email=email,password=senha,first_name=nome,last_name=sobrenome)
    user.save()
    return redirect('login')
@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
