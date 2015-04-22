from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Minerva.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^registroEntidad/', 'Entidad.views.formularioRegistro', name="formularioRegistro"),
    url(r'^registroPeticion/', 'Entidad.views.registroPeticion', name="registroPeticion"),
    url(r'^loginPeticion/', 'Entidad.views.iniciarSesionPeticion', name="iniciarSesionPeticion"),
    url(r'^logout/', 'Entidad.views.logout_view', name="Logout"),
    url(r'^crear/', 'Entidad.views.registrarEntidad', name="registrarEntidad"),
    url(r'^crearDistincion/', 'Entidad.views.crearDistincion', name="crearDistincion"),
    url(r'^eliminarDistincion/', 'Entidad.views.eliminarDistincion', name="eliminarDistincion"),
    url(r'^crearEmprendedor/', 'EmprendedorPremio.views.crearEmprendedor', name="crearEmprendedor"),
    url(r'^emprendedorPremio/', include('EmprendedorPremio.urls')),
    url(r'^empresarioBenemerito/', include('EmpresarioBenemerito.urls')),
    #---- url para combos anidados
    url(r'^getMunicipios/', 'Entidad.views.chainedMunicipio', name="Municipios"),
    url(r'^getCorregimientos/', 'Entidad.views.chainedCorregimiento', name="Corregimientos"),
    #-----------------------------

    url(r'^inicio/', 'Entidad.views.home', name="home"),
    url(r'^crearAdjunto/(?P<tipo>[\d]+)', 'Entidad.views.crearAdjuntoEmpresa', name="crearAdjuntoEmpresa"),
    url(r'^getAdjuntosEmpresa/(?P<tipo>[\d]+)', 'Entidad.views.consultarAdjuntoEmpresa', name="consultarAdjuntoEmpresa"),

    url(r'^crearAdjuntoOtros/(?P<tipo>[\d]+)', 'Entidad.views.crearAdjuntoOtrosEmpresa', name="crearAdjuntoOtrosEmpresa"),
    url(r'^getAdjuntoOtros/', 'Entidad.views.consultarAdjuntosOtrosEmpresa', name="consultarAdjuntosOtrosEmpresa"),
    url(r'^deleteAdjuntoOtros/', 'Entidad.views.borrarAdjuntosOtroEmpresa', name="borrarAdjuntosOtroEmpresa"),
    
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)