from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Minerva.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^crearDistincion/', 'EmprendedorPremio.views.crearDistincion', name="crearDistincion"),
    url(r'^guardarAdjuntos/', 'EmprendedorPremio.views.guardarAdjuntos', name="guardarAdjuntos"),
    url(r'^crearAdjunto/(?P<tipo>[\d]+)', 'EmprendedorPremio.views.crearAdjuntoEmprendedor', name="crearAdjuntoEmprendedor"),
    url(r'^getAdjuntos/(?P<tipo>[\d]+)', 'EmprendedorPremio.views.consultarAdjuntoEmprendedor', name="consultarAdjuntoEmprendedor"),
    url(r'^eliminarDistincion/', 'EmprendedorPremio.views.eliminarDistincion', name="eliminarDistincion"),
    
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)