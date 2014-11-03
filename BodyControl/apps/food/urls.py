
from django.shortcuts import render, render_to_response,RequestContext
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from .views import *
from .ajax import *
 
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
   				
   					url(r'^foods/(?P<estado_id>[0-9]+)/$', 'BodyControl.apps.food.views.load_foods', name='foods'),
 
)