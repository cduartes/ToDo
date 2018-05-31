from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Tarea
from datetime import date
from django.utils import formats

# Create your views here.
@login_required()
def index(request):
    if request.user:
        return redirect('tareas')
    else:
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
        tarea.fechaInicio = request.POST.get('fecha_inicio')
        tarea.fechaTermino = request.POST.get('fecha_termino')
        tarea.usuario = request.user
        tarea.save()
    return redirect('tareas')

#TODO
@login_required
def actualizar_tarea(request):
    if request.method == 'POST':
        tarea = Tarea.objects.get(pk=request.POST.get("hidden_id"))
        #tarea = Tarea.objects.filter(id = request.POST.get('hidden_id'))
        if tarea.usuario == request.user:
            tarea.titulo = request.POST.get('titulo')
            tarea.descripcion = request.POST.get('descripcion')
            tarea.fechaInicio = request.POST.get('fecha_inicio')
            tarea.fechaTermino = request.POST.get('fecha_termino')
            tarea.save()
    return redirect('tareas')
#TODO
@login_required
def eliminar_tarea(request):
    if request.method == 'GET':
        tarea = Tarea.objects.get(pk=request.GET.get("id"))
        if tarea.usuario == request.user:
            tarea.delete()
    return redirect('tareas')
#TODO
@login_required
def calendario(request):
    tareas = Tarea.objects.filter(usuario = request.user)
    return render(request, 'calendario.html', { 'tareas': tareas})

@login_required
def tarea(request):
    if request.method == 'GET':
        tarea = Tarea.objects.get(pk=request.GET.get("id"))
        return render(request, 'tarea.html', { 'tarea': tarea })