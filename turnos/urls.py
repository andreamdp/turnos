# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from aplicacion.views import *
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'turnos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

     # Uncomment the next line to enable the admin:
 (r'^admin/app/estudiante/$', jqgrid_estudiante),#cargar el template listado de estudiantes.
 (r'^admin/app/estudiante/ver/$', ver_jqgrid_estudiante),#cargar el jqgrid con la data del modelo estudiante, asi como busquedas y ordenar.
 (r'^admin/app/estudiante/obtener_carreras/$', obtener_carreras),#obtener las carreras de manera dinámica
 (r'^admin/app/estudiante/master/$', master_jqgrid_estudiante),#ejecutar operaciones de agregar, modificar o eliminar registros
 (r'^admin/', include(admin.site.urls)),
 (r'^', index),
 (r'^media/(.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT }),
 
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()

