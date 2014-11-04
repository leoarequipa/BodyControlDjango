
from django.shortcuts import render, render_to_response,RequestContext
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from .views import *
from .ajax import *
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
   	url(r'^history/(?P<dia_id>[0-9]+)/$', 'BodyControl.apps.estado.views.load_history', name='history'),
    url(r'^add_status/$', 'BodyControl.apps.estado.views.add',name='add_status'),   
    url(r'^edit_status/(?P<estado_id>[0-9]+)/$', 'BodyControl.apps.estado.views.edit',name='edit_status'),
    url(r'^delete_status/(?P<estado_id>[0-9]+)/$', 'BodyControl.apps.estado.views.delete',name='delete_status'),      
)