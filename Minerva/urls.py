from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Minerva.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/presupuesto/(?P<pk>[\d]+)', 'Vistas.views.presupuesto', name="Presupuesto"),
	url(r'^admin/presupuesto/rubro/(?P<pk>[\d]+)/(?P<proyecto>[\d]+)', 'Vistas.views.rubroDetalle', name="DetalleRubro"),
	url(r'^admin/presupuesto/rubro/eliminarPago/(?P<pk>[\d]+)', 'Vistas.views.eliminarPagoRubro', name='EliminarPagoRubro'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^usuarios/', include('Entidad.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^password/reset/$', 'django.contrib.auth.views.password_reset', 
        {'post_reset_redirect' : '/password/reset/done/'}, name="password_reset"),

    url(r'^password/reset/done/$', 'django.contrib.auth.views.password_reset_done'),

    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/password/done/'}),
    
    url(r'^password/done/$', 'django.contrib.auth.views.password_reset_complete'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
