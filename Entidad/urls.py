from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Minerva.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^registroEntidad/', 'Entidad.views.formularioRegistro', name="formularioRegistro"),
    url(r'^registroPeticion/', 'Entidad.views.registroPeticion', name="registroPeticion"),
    url(r'^loginPeticion/', 'Entidad.views.iniciarSesionPeticion', name="iniciarSesionPeticion"),
    url(r'^crear/', 'Entidad.views.registrarEntidad', name="registrarEntidad"),
    
    #---- url para combos anidados
    url(r'^getMunicipios/', 'Entidad.views.chainedMunicipio', name="Municipios"),
    url(r'^getCorregimientos/', 'Entidad.views.chainedCorregimiento', name="Corregimientos"),
    #-----------------------------

    url(r'^inicio/', 'Entidad.views.home', name="home"),
    
)