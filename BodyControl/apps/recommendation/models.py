from django.db import models

# Create your models here.
class Recommendation(models.Model):
	titulo = models.CharField(max_length=50,default="")
	contenido = models.TextField(max_length=300000,default="")
	photo = models.ImageField(upload_to="recommendation/",null=True, blank=True)