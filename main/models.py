from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length = 255)
    descripcion = models.CharField(max_length = 255)
    fechaInicio = models.DateField(default=date.today)
    fechaTermino = models.DateField(default=date.today)
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
