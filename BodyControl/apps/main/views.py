from django.shortcuts import render, render_to_response,RequestContext,redirect 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse

from django.template.context import RequestContext
from django.contrib.auth.models import User
from .forms import FormRegister,BodyStart
from .models import DatosUser
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import TemplateView,ListView
 
from django.core import serializers
import simplejson 
import json
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.template import RequestContext




# Create your views here.
@login_required
def home(request):
    return render(request, "main/index.html")

@login_required
def load_perfil(request):
  
    user = request.user
    if request.POST:
        form = BodyStart(request.POST)
        if form.is_valid():
            
            post = form.save(commit=False)
            post.user = user
            post.save()
            return redirect(reverse("home"))
    else:
       # estado ="Con datos"
        #u = DatosUser.objects.get( user = user)
        #form = BodyStart(instance=u)
 
        form = BodyStart()
     
        estado ="Sin datos"
    return render(request, "user/load_perfil.html", {'form': form,'estado':estado})

 


def register(request):
    if request.POST:
        #form =PostForm(request.POST)
        form = FormRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
 
            # At this point, user is a User object that has already been saved
            # to the database. You can continue to change its attributes
            # if you want to change other fields.
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.is_staff=True
            user.is_superuser=True
            # Save new user attributes
            user.save()
          
            
          #  form = Buscar()
            ##return render(request, "login.html", {'form': form,'estado':"registrado"})
            return redirect(reverse("login"))
        else:
            form = FormRegister()
            templa= "register"
            return redirect(reverse("register"))
 
    else:
        form = FormRegister()
        templa= "register"
    return render(request, "user/register.html", {'form': form,'templa':templa})

def modify_profile(request):
    user = request.user
    if request.POST:
        form = BodyStart(request.POST)
        if form.is_valid():
            
            post = form.save(commit=False)
            post.user = user
            post.save()
            return redirect(reverse("home"))
    else:
        u = DatosUser.objects.get( user = user)
        form = BodyStart()
        form.edad = u.edad
        form.estatura = u.estatura
        estado ="Con datos"
    return render(request, "user/load_perfil.html", {'form': form,'datos':u,'estado':estado})

def load_users(request):
    users = User.objects.all()
    return render(request, "main/bodyPublic.html", {'usuarios': users})



 

class Datos(ListView):
    model = User
    template_name = 'user/load_perfil.html'
    context_object_name = 'usuarios'



class Hello(TemplateView):
    def get(self,request,*args, **kwargs):
        id = request.GET['id']
       # url = equest.GET['url']
        u = DatosUser.objects.filter( user_id = id )
        #data = serializers.serialize('json',u)
        html = render_to_string('user/ajax/misEstados.html', {'misDatos': u }, context_instance=RequestContext(request))
        #json_data = '{"hello": "world", "foo": "bar"}' 
        #data = json.loads(json_data)
        #return HttpResponse(html,content_type='application/json')
        #return render_to_response("user/ajax/misEstados.html", {"misDatos": json.dumps(data)})
        return HttpResponse(html)


 