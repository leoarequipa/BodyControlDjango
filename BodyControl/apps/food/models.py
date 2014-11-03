from django.db import models
from BodyControl.apps.estado.models import Estado
# Create your models here.
class Alimento(models.Model):
    estado = models.ForeignKey(Estado)
    nombre = models.CharField(max_length=50,default="")
    calorias = models.FloatField(max_length=20,default=0.0)
    tipo = models.CharField(max_length=50,default="")
    puntaje = models.IntegerField(default=0)
    eliminado = models.CharField(default='', max_length=50)
    comentario = models.TextField(default='',max_length=800)
    situacion_comida = models.CharField(default='', max_length=50)
    photo_food = models.ImageField(upload_to="foods/",null=True, blank=True)