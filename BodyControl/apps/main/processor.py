from django.contrib.auth.models import User
from BodyControl.apps.main.models import *
from BodyControl.apps.estado.models import *
from BodyControl.apps.day.models import *
from BodyControl.apps.food.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
	#dias = Dia.objects.all()
	#comidas = Alimento.objects.all()
	#estados = DatosUser.objects.all()
	#usuarios = User.objects.all()
	return {'usuarios': DatosUser.objects.all(),'comidas':Alimento.objects.all
	,'dias': Dia.objects.all(),'estados':Estado.objects.all()}