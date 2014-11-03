from django.contrib.auth.models import User
from BodyControl.apps.main.models import *
from BodyControl.apps.estado.models import *
from BodyControl.apps.day.models import *
from BodyControl.apps.food.models import *
from BodyControl.apps.recommendation.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def recomendation(request):
 
	return {'recomendaciones': Recommendation.objects.all()}