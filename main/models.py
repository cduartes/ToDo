from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Estado(models.Model):
    nombre = models.CharField(max_length = 255)
    def __str__(self):
        return self.nombre
class Tarea(models.Model):
    titulo = models.CharField(max_length = 255)
    descripcion = models.CharField(max_length = 255)
    fechaInicio = models.DateField(default=date.today)
    fechaTermino = models.DateField(default=date.today)
    estado = models.ForeignKey(Estado, on_delete = models.PROTECT)
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return self.titulo