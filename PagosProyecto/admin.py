from django.contrib import admin
from django.http import HttpResponse
from .models import PagosProyecto, AdjuntoSolicitud, TipoEjecucion, AdjuntoEgreso
# Register your models here.

class AdjuntoSolicitudInline(admin.StackedInline):
	model = AdjuntoSolicitud
	extra = 1

class AdjuntoEgresoInline(admin.StackedInline):
	model = AdjuntoEgreso
	extra = 1

class PagoProyectoAdmin(admin.ModelAdmin):
	inlines = [AdjuntoSolicitudInline, AdjuntoEgresoInline, ]

	def response_change(self, request, obj, post_url_continue='../%s/'):
		resp = super(PagoProyectoAdmin, self).response_change(request, obj)
		if request.POST.has_key("_popup"):
			return HttpResponse('<script type="text/javascript">window.close();window.opener.location.reload(true);</script>')# % \
				#(escape(obj._get_pk_val()),escape(obj)))
		return resp 
		

admin.site.register(PagosProyecto, PagoProyectoAdmin)
admin.site.register(TipoEjecucion)