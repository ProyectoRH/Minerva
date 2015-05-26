from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'Vistas.views.principalPremio', name="adminPremio"),
    url(r'^emprendedores/', 'Vistas.views.listarEmprendedores', name="listarEmprendedores"),
    url(r'^emprendedor/(?P<pk>[\d]+)', 'Vistas.views.detallesEmprendedor', name="detallesEmprendedor"),
    
    url(r'^entidades/', 'Vistas.views.listarEmpresas', name="listarEmpresas"),
    url(r'^entidad/(?P<pk>[\d]+)', 'Vistas.views.detallesEntidad', name="detallesEntidad"),

    url(r'^gremios/', 'Vistas.views.listarGremios', name="listarEmpresas"),
    url(r'^gremio/(?P<pk>[\d]+)', 'Vistas.views.detallesGremio', name="detallesEntidad"),
    url(r'^empresario/(?P<pk>[\d]+)', 'Vistas.views.detalleEmpresarioGremio', name="detallesEmpresario"),
)
