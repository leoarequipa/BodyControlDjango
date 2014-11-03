from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Dia(models.Model):
	persona = models.ForeignKey(User)
	fecha = models.DateTimeField()
	peso_dia_ant = models.FloatField(max_length=20,default=0.0)
	peso_acumulado = models.FloatField(max_length=30,default=0.0)
	autocritica = models.CharField(max_length=50,default="")
	eliminado = models.CharField(default='', max_length=50)
	situacion_dia = models.CharField(default='', max_length=50)

