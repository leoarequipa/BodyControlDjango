from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

 
urlpatterns = patterns('',
 	url(r'^', include('BodyControl.apps.main.urls')),
 	url(r'^dias/', include('BodyControl.apps.day.urls')),
 	url(r'^status/', include('BodyControl.apps.estado.urls')),
 	url(r'^foods/', include('BodyControl.apps.food.urls')),
	url(r'^users/login/', "django.contrib.auth.views.login", dict(template_name="login.html"), name="login"),
	url(r'^users/logout/', "django.contrib.auth.views.logout", {"next_page": "/"}, name="logout"),
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf import settings

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
    )