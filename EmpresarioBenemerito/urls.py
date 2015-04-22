from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Minerva.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^crearEmpresario/', 'EmpresarioBenemerito.views.crearEmpresario', name="crearEmpresario"),
    url(r'^getEmpresario/', 'EmpresarioBenemerito.views.getEmpresario', name="getEmpresario"),
    url(r'^actualizarEmpresario/', 'EmpresarioBenemerito.views.actualizarEmpresario', name="actualizarEmpresario"),
    url(r'^crearAdjunto/(?P<tipo>[\d]+)', 'EmpresarioBenemerito.views.crearAdjuntoEmpresario', name="crearAdjuntoEmpresario"),
    url(r'^consultarAdjuntoEmpresario/(?P<tipo>[\d]+)', 'EmpresarioBenemerito.views.consultarAdjuntoEmpresario', name="consultarAdjuntoEmpresario"),
    url(r'^crearOrganizacion/', 'EmpresarioBenemerito.views.crearOrganizacion', name="crearOrganizacion"),
    url(r'^eliminarOrganizacion/', 'EmpresarioBenemerito.views.eliminarOrganizacion', name="eliminarOrganizacion"),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)