from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tarea, Estado, Tipo

# Create your views here.
def root(request):
    return redirect('tareas')

@login_required()
def index(request):
    return redirect('tareas')

"""
Display all Tareas

If authentificated user is admin of site, return all Tareas.
Else, just return Tareas he owns.
---
View will only show active Tareas, hiding others untill the GET parameter "all=TRUE" is send
"""
@login_required
@require_GET
def tareas(request):
    admin = request.user.groups.filter(name='usuario_admin').exists()
    estados = Estado.objects.all().order_by('nombre')
    tipos = Tipo.objects.all().order_by('nombre')
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
        return render(request, 'tareas.html', { 'tareas': tareas, 'estados': estados, 'tipos': tipos, 'all': all_tareas})

"""
Create Tarea
"""
@login_required
@require_POST
def crear_tarea(request):
    #tarea = Tarea.objects.create() #crea un elemento automaticamente en la bd con valores nulos
    tarea = Tarea() # crea el objeto en memoria
    tarea.titulo = request.POST.get('titulo')
    tarea.descripcion = request.POST.get('descripcion')
    tarea.fechaInicio = request.POST.get('fecha_inicio')
    tarea.fechaTermino = request.POST.get('fecha_termino')
    tarea.tipo = Estado.objects.get(pk=request.POST.get('tipo'))
    tarea.estado = Estado.objects.get(pk=request.POST.get('estado'))
    tarea.usuario = request.user
    tarea.save()
    return redirect('tareas')

"""
Update Tarea's data only if user is owner.
"""
@login_required
@require_POST
def actualizar_tarea(request):
    tarea = Tarea.objects.get(pk=request.POST.get("hidden_id"))
    if tarea.usuario == request.user:
        tarea.titulo = request.POST.get('titulo')
        tarea.descripcion = request.POST.get('descripcion')
        tarea.fechaInicio = request.POST.get('fecha_inicio')
        tarea.fechaTermino = request.POST.get('fecha_termino')
        tarea.tipo = Estado.objects.get(pk=request.POST.get('tipo'))
        tarea.estado = Estado.objects.get(pk=request.POST.get('estado'))
        tarea.save()
    return redirect('tareas')

"""
Delete specific tarea, only if authentificated user is owner or admin
"""
@login_required
@require_GET
def eliminar_tarea(request):
    admin_bool = request.user.groups.filter(name='usuario_admin').exists()
    tarea = Tarea.objects.get(pk=request.GET.get("id"))
    if admin_bool:
        tarea.delete()
    elif tarea.usuario == request.user:
        tarea.delete()
    return redirect('tareas')

"""
Display as calender all Tareas if user is admin.
Else, show only Tareas owned.
"""
@login_required
def calendario(request):
    admin = request.user.groups.filter(name='usuario_admin').exists()
    if admin:
        tareas = Tarea.objects.filter(estado = 1)
        return render(request, 'calendario_admin.html', { 'tareas': tareas})
    else:
        tareas = Tarea.objects.filter(usuario = request.user, estado = 1)
        return render(request, 'calendario.html', { 'tareas': tareas})

"""
Display data of a single Tarea
"""
@login_required
@require_GET
def tarea(request):
    estados = Estado.objects.all().order_by('nombre')
    tipos = Tipo.objects.all().order_by('nombre')
    tarea = Tarea.objects.get(pk=request.GET.get("id"))
    if request.user == tarea.usuario:
        return render(request, 'tarea.html', { 'tarea': tarea, 'estados': estados, 'tipos': tipos })
    else:
        return HttpResponse("Error al obtener elemento. Credenciales no coinciden.")