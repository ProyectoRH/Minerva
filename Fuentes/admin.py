from django.contrib import admin
from .models import Fuente, TipoRubro, EstadoFuente
from AdjuntosFuente.models import AdjuntoFuente
# Register your models here.

class AdjuntoFuenteInline(admin.StackedInline):
	model = AdjuntoFuente
	extra = 1

class FuenteAdmin(admin.ModelAdmin):
	inlines = (AdjuntoFuenteInline, )


admin.site.register(TipoRubro)
admin.site.register(EstadoFuente)
admin.site.register(Fuente, FuenteAdmin)