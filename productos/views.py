from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Polera
from .forms import PoleraForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages

# Create your views here.

@login_required
def listar_poleras(request):
    poleras = Polera.objects.all()
    return render(request,'listar_poleras.html', {'poleras': poleras})

@login_required
def crear_polera(request):
    if request.method == 'POST':
        form = PoleraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_poleras')
    else:
        form = PoleraForm()
    return render(request, 'crear_polera.html', {'form': form})

@login_required
def editar_polera(request, pk):
    polera = get_object_or_404(Polera, pk=pk)
    if request.method == 'POST':
        form = PoleraForm(request.POST, request.FILES, instance=polera)
        if form.is_valid():
            form.save()
            return redirect('listar_poleras')
    else:
        form = PoleraForm(instance=polera)
    return render(request, 'editar_polera.html', {'form': form})

@login_required
def eliminar_polera(request, pk):
    polera = get_object_or_404(Polera, pk=pk)
    if request.method == 'POST':
        polera.delete()
        messages.success(request, 'Polera eliminada correctamente.')
        return redirect('listar_poleras')
    return render(request, 'eliminar_polera.html', {'polera': polera})

def registro_usuario(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('login')  # Redirigir al login después de registro
    else:
        form = UserCreationForm()
    
    return render(request, 'registro_usuario.html', {'form': form})

@login_required
def editar_usuario(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('editar_usuario') 
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, 'editar_usuario.html', {'form': form})