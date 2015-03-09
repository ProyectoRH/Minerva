from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from django.http import HttpResponse
from datetime import date

from .models import Proyecto

from Fuentes.models import Fuente
from EntidadVsProyecto.models import EntidadVsProyecto
from AdjuntosProyecto.models import AdjuntoProyecto
from InvestigadorVsProyecto.models import InvestigadorVsProyecto
from Alertas.models import Alertas
from PagosProyecto.models import PagosProyecto
from ResultadosProyecto.models import Producto

# Register your models here.

class EntidadVsProyectoInline(admin.StackedInline):
	model = EntidadVsProyecto
	extra = 1
	suit_classes = 'suit-tab suit-tab-entidad'

class AdjuntoProyectoInline(admin.StackedInline):
	model = AdjuntoProyecto
	extra = 1
	suit_classes = 'suit-tab suit-tab-adjuntoEjecucion'

class InvestigadorProyectoInline(admin.StackedInline):
	model = InvestigadorVsProyecto
	raw_id_fields = ('investigador',)
	extra = 1
	suit_classes = 'suit-tab suit-tab-investigador'

class FuenteInline(admin.StackedInline):
	model = Fuente
	extra = 1
	suit_classes = 'suit-tab suit-tab-fuentes'

class AlertasInline(admin.StackedInline):
	model = Alertas
	extra = 1
	suit_classes = 'suit-tab suit-tab-alertas'	

class PagosProyectoInline(admin.StackedInline):
	model = PagosProyecto
	extra = 1
	suit_classes = 'suit-tab suit-tab-pagos'

class ResultadosProyectoInline(admin.StackedInline):
	model = Producto
	extra = 1
	suit_classes = 'suit-tab suit-tab-resultados'

class ProyectoInline(admin.ModelAdmin):

	inlines = [EntidadVsProyectoInline, InvestigadorProyectoInline, AdjuntoProyectoInline, FuenteInline, AlertasInline, PagosProyectoInline, ResultadosProyectoInline, ]
	filter_horizontal = ('grupos_investigacion',)
	list_display = ['codigo_interno_proyecto','titulo','fecha_inicio','tipo_proyecto','duracion','categoria_colciencias',]
	search_fields = ['codigo_interno_proyecto','titulo','fecha_inicio','palabras_clave',]

	fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['codigo_interno_proyecto','tipo_proyecto', 'estado', 'titulo', 'duracion', 'fecha_inicio', 'tipo_investigacion', 'grupos_investigacion', 'categoria_colciencias', 'linea_investigacion', 'resumen', 'palabras_clave', 'departamento', 'municipio', 'corregimiento', 'planteamiento_problema', 'estado_arte', 'objetivos', 'metodologia', 'impacto_esperado',]
        }),
    ]

	suit_form_tabs = (('general', 'Proyecto'), ('entidad', 'Entidad'), ('investigador', 'Personas'), ('fuentes', 'Fuentes'), ('adjuntoEjecucion', 'Adjuntos'), ('alertas', 'Alertas'), ('pagos', 'Pagos'), ('resultados', 'Resultados'))

	def save_model(self, request, obj, form, change):
		obj.digitador = request.user
		if obj.codigo_interno_proyecto == None or obj.codigo_interno_proyecto == '':
			d = date.today()
			obj.codigo_interno_proyecto = str(obj.pk) + str(d.month) + str(d.year)
		obj.save()

	@property
	def media(self):
		media = super(ProyectoInline, self).media
		js = ["js/test.js",]
		media.add_js(js)
		return media
    


admin.site.register(Proyecto, ProyectoInline)
