from django.shortcuts import render, render_to_response,RequestContext,redirect 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.models import User
 
from .models import Alimento
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, authenticate, logout
#from BodyControl.apps.food.managers import Pasta


@login_required()
def load_foods(request,estado_id):
	foods = Alimento.objects.filter(estado=estado_id)
	#f = Pasta();
	#foods = Alimento.f.all()
	 
	return render(request, "food/foods.html", {'foods':foods})

@login_required()
def add(request):
    if request.POST:
        form = Estado(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect(reverse("home"))
    else:
        form = Estado()
    return render(request, "status/add_status.html", {'form_status':form})
@login_required()
def edit(request,food_id):
    if request.POST:
        form = Estado(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect(reverse("home"))
    else:
        form = Estado()
    return render(request, "status/add_status.html", {'form_status':form})
    
@login_required()
def delete(request,food_id):
    if request.POST:
        form = Estado(request.POST)
        if form.is_valid():            
            post = form.save(commit=False)
            post.save()
            return redirect(reverse("home"))
    else:
        form = Estado()
    return render(request, "status/add_status.html", {'form_status':form})