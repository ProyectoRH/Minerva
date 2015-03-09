from django.contrib import admin
from django.http import HttpResponse
from .models import Fuente, TipoRubro, EstadoFuente
from AdjuntosFuente.models import AdjuntoFuente
# Register your models here.

class AdjuntoFuenteInline(admin.StackedInline):
	model = AdjuntoFuente
	extra = 1

class FuenteAdmin(admin.ModelAdmin):
	inlines = (AdjuntoFuenteInline, )

	def response_change(self, request, obj, post_url_continue='../%s/'):
		resp = super(FuenteAdmin, self).response_change(request, obj)
		if request.POST.has_key("_popup"):
			return HttpResponse('<script type="text/javascript">window.close();window.opener.location.reload(true);</script>')# % \
				#(escape(obj._get_pk_val()),escape(obj)))
		return resp 


admin.site.register(TipoRubro)
admin.site.register(EstadoFuente)
admin.site.register(Fuente, FuenteAdmin)