from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UsuarioRegistroForm, UsuarioEdicionForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = UsuarioRegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:home')
    else:
        form = UsuarioRegistroForm()
    return render(request, 'usuarios/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blog:home')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'usuarios/profile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UsuarioEdicionForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('usuarios:profile')
    else:
        form = UsuarioEdicionForm(instance=request.user)
    return render(request, 'usuarios/edit_profile.html', {'form': form})
