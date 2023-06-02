from django.db import models

# Create your models here.
class Comunicado(models.Model):
    titulo = models.TextField(max_length=100)
    detalle = models.TextField(max_length=100)
    #nivel =
    #categoria
    fecha_envio = models.DateTimeField()
    fecha_ultima_modificacion = models.DateTimeField()
    #publicado_por = 

class Categoria(models.Model):
    nombre = models.TextField(max_length=100)
    descripcion = models.TimeField(max_length=1000)