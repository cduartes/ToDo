from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Tarea

# Create your views here.
@login_required()
def index(request):
    return render(request, 'home.html')
    #return HttpResponse("HolaMundo Django!")

@login_required
def tareas(request):
    #tareas = Tarea.objects.all()
    tareas = Tarea.objects.filter(usuario = request.user)
    return render(request, 'tareas.html', { 'tareas': tareas})

@login_required
def crear_tarea(request):
    if request.method == 'POST':
        #tarea = Tarea.objects.create() #crea un elemento automaticamente en la bd con valores nulos
        tarea = Tarea() # crea el objeto en memoria
        print(request.POST)
        tarea.titulo = request.POST.get('titulo')
        tarea.descripcion = request.POST.get('descripcion')
        tarea.usuario = request.user
        tarea.save()
    return redirect('tareas')

#TODO
@login_required
def actualizar_tarea(request):
    if request.method == 'POST':
        tarea = Tarea.objects.filter(id = request.POST.get('hidden_id'))
        if tarea.usuario == request.user:
            tarea.titulo = request.POST.get('titulo')
            tarea.descripcion = request.POST.get('descripcion')
            tarea.save()
    return redirect('tareas')
#TODO
@login_required
def eliminar_tarea(request):
    if request.method == 'POST':
        tarea = Tarea.objects.filter(id = request.POST.get('hidden_id'))
        if tarea.usuario == request.user:
            tarea.delete()
    return redirect('tareas')
#TODO
@login_required
def calendario(request):
    tareas = Tarea.objects.filter(usuario = request.user)
    return render(request, 'calendario.html', { 'tareas': tareas})