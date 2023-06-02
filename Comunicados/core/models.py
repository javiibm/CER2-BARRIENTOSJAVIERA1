from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.TextField(max_length=100)
    descripcion = models.TimeField(max_length=1000)

class Comunicado(models.Model):
    titulo = models.TextField(max_length=100)
    detalle = models.TextField(max_length=100)
    #nivel =
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_envio = models.DateTimeField()
    fecha_ultima_modificacion = models.DateTimeField()
    #publicado_por = 