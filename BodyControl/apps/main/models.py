from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#from sorl.thumbnail import ImageField

class DatosUser(models.Model):
	user = models.OneToOneField(User)
	edad = models.IntegerField(max_length=40,default=0.0)
	sexo = models.CharField(default='', max_length=50)
	estatura = models.IntegerField(max_length=30,default=0.0)
	peso_inicial = models.FloatField(max_length=20,default=0.0)
	peso_ideal = models.FloatField(max_length=20,default=0.0)
	peso_actual = models.FloatField(max_length=20,default=0.0)
	eliminado = models.CharField(default='', max_length=50)
	situacion_general = models.CharField(default='', max_length=50)
	avatar = models.ImageField( upload_to="perfiles/",null=True, blank=True)
	#thumbnail = ImageSpecField(source='photo',
     #                                 processors=[ResizeToFill(50, 50)],
      #                                format='PNG',
       #                               options={'quality': 60})
