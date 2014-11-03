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

from django.template import RequestContext



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

 