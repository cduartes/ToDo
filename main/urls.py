from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #url(r'^login/$', auth_views.login, name='login'),
    #url(r'^logout/$', auth_views.logout, name='logout'),
    path('home/', views.index, name='home'),
    path('tareas/',views.tareas, name='tareas'),

    path('crear_tarea', views.crear_tarea, name="crear_tarea"),
    path('calendario', views.calendario, name="calendario"),
    path('tarea', views.tarea, name="tarea"),
    path('actualizar_tarea', views.actualizar_tarea, name="actualizar_tarea"),
    path('eliminar_tarea', views.eliminar_tarea, name="eliminar_tarea"),
]