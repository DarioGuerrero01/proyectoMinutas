from django.db import models
from django.db.models.base import Model

# Create your models here.
class Minuta(models.Model):
    titulo=models.CharField(max_length=150)
    secretario=models.CharField(max_length=150)
    texto=models.CharField(max_length=5000)
    fecha_reunion=models.CharField(max_length=10)
    hora_inicio=models.CharField(max_length=5)
    hora_fin=models.CharField(max_length=5)
    asistentes=models.CharField(max_length=5000)
