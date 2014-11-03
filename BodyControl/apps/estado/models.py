from django.db import models
from django.contrib.auth.models import User
from BodyControl.apps.day.models import Dia
# Create your models here.


class Estado(models.Model):

	total_calorias = models.IntegerField(max_length=40,default=True)
	comida = models.CharField(default='', max_length=50)
	day = models.ForeignKey(Dia,null=True)
	eliminado = models.CharField(default='', max_length=50)
