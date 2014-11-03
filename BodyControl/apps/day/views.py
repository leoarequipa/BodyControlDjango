from django.shortcuts import render, render_to_response,RequestContext,redirect 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.models import User
 
from .models import Dia
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, authenticate, logout
 


@login_required()
def load_status(request,user_id):

	dias = Dia.objects.filter(persona=user_id)

	return render(request, "day/my.html", {'dias':dias})

