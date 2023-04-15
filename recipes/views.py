from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Pet


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('já existe um usuário com esse nome!')
        
        user = User.objects.create_user(username=username, email=email, 
                                        password=senha)
        user.save()

        return redirect('login')
    

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)

            return redirect('perfis_pet')
        else:
            messages.error(request, 'Usuário e senha inválido, Favor tentar novamente.')
        return redirect('login')


@login_required(login_url="/auth/login/")
def plataforma(request):
    return render(request, 'pet.html')


def perfis_pet(request):
    pet = Pet.objects.filter(active=True)
    return render(request, 'pet.html', {'pet': pet})


def todo_list(request):
    return render(request, 'todo_list.html', {})