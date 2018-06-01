from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.models import Group, User
from .models import Tarea, Estado
from datetime import date
from django.utils import formats

# Create your views here.
@login_required()
def index(request):
    return redirect('tareas')
    #return HttpResponse("HolaMundo Django!")

"""
retorna todas las tareas.
Si el usuario autentificado es administrador del sitio, retorna todas las tareas.
Si el usuario autentificado no es administrador, retorna solo las tareas que él ha creado.
---
La vista mostrará por defecto solo las tareas activas, ocultando las no activas a menos que se reciba el parámetro "all=TRUE"
"""
@login_required
@require_GET
def tareas(request):
    admin = request.user.groups.filter(name='usuario_admin').exists()
    estados = Estado.objects.all().order_by('nombre')
    all_tareas = 'FALSE'
    if request.GET.get("all"):
        if request.GET.get("all") == 'TRUE' or request.GET.get("all") == 'true':
            all_tareas = 'TRUE'
            if admin:   tareas = Tarea.objects.all().order_by('fechaInicio')
            else:   tareas = Tarea.objects.filter(usuario = request.user).order_by('fechaInicio')
        else:
            if admin: tareas = Tarea.objects.filter(estado = 1).order_by('fechaInicio')
            else:   tareas = Tarea.objects.filter(usuario = request.user, estado = 1).order_by('fechaInicio')
    else:
        if admin:   tareas = Tarea.objects.filter(estado = 1).order_by('fechaInicio')
        else:   tareas = Tarea.objects.filter(usuario = request.user, estado = 1).order_by('fechaInicio')
    if admin:
        usuarios = User.objects.all()
        return render(request, 'tareas_admin.html', { 'tareas': tareas, 'estados': estados, 'all': all_tareas, 'usuarios': usuarios})
    else:
        return render(request, 'tareas.html', { 'tareas': tareas, 'estados': estados, 'all': all_tareas})

@login_required
@permission_required('main.can_add_tarea')
@require_POST
def crear_tarea(request):
    #tarea = Tarea.objects.create() #crea un elemento automaticamente en la bd con valores nulos
    tarea = Tarea() # crea el objeto en memoria
    tarea.titulo = request.POST.get('titulo')
    tarea.descripcion = request.POST.get('descripcion')
    tarea.fechaInicio = request.POST.get('fecha_inicio')
    tarea.fechaTermino = request.POST.get('fecha_termino')
    tarea.estado = Estado.objects.get(pk=request.POST.get('estado'))
    tarea.usuario = request.user
    tarea.save()
    return redirect('tareas')

@login_required
@permission_required('main.can_change_tarea')
@require_POST
def actualizar_tarea(request):
    tarea = Tarea.objects.get(pk=request.POST.get("hidden_id"))
    #tarea = Tarea.objects.filter(id = request.POST.get('hidden_id'))
    if tarea.usuario == request.user:
        tarea.titulo = request.POST.get('titulo')
        tarea.descripcion = request.POST.get('descripcion')
        tarea.fechaInicio = request.POST.get('fecha_inicio')
        tarea.fechaTermino = request.POST.get('fecha_termino')
        tarea.estado = Estado.objects.get(pk=request.POST.get('estado'))
        tarea.save()
    return redirect('tareas')

@login_required
@permission_required('main.can_delete_tarea')
@require_GET
def eliminar_tarea(request):
    tarea = Tarea.objects.get(pk=request.GET.get("id"))
    if tarea.usuario == request.user:
        tarea.delete()
    return redirect('tareas')

@login_required
def calendario(request):
    admin = request.user.groups.filter(name='usuario_admin').exists()
    if admin:
        tareas = Tarea.objects.all()
        return render(request, 'calendario_admin.html', { 'tareas': tareas})
    else:
        tareas = Tarea.objects.filter(usuario = request.user)
        return render(request, 'calendario.html', { 'tareas': tareas})

@login_required
@permission_required('main.can_change_tarea')
@require_GET
def tarea(request):
    estados = Estado.objects.all().order_by('nombre')
    tarea = Tarea.objects.get(pk=request.GET.get("id"))
    return render(request, 'tarea.html', { 'tarea': tarea, 'estados': estados })