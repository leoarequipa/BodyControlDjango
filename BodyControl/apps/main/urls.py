
from django.shortcuts import render, render_to_response,RequestContext
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from .views import *
from django.conf.urls import patterns, include, url

 
urlpatterns = patterns('',
            url(r'^$','BodyControl.apps.main.views.load_perfil',name='load_perfil'),
					 url(r'^accounts/profile/$','BodyControl.apps.main.views.home',name='home'),  
   					url(r'^register/$', 'BodyControl.apps.main.views.register',name='register'),  
   					url(r'^load_perfil/$', 'BodyControl.apps.main.views.load_perfil',name='load_perfil'),  
   					url(r'^load_users/$', 'BodyControl.apps.main.views.load_users',name='load_users'),  
   					
                    #url(r'^load_dates/$', Datos.as_view()),  
                    #url(r'^load/$', 'BodyControl.apps.main.views.datos',name='load_users'), 
                    #url(r'^load_datos/$', 'BodyControl.apps.main.views.hello',name='load_datos'), 
              url(r'^load_datos/$', Hello.as_view()), 
)