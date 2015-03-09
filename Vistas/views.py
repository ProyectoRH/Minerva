from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from Proyecto.models import Proyecto
from Fuentes.models import Fuente, TipoRubro
from PagosProyecto.models import PagosProyecto
from EntidadVsProyecto.models import EntidadVsProyecto
from Entidad.models import Entidad

# Create your views here.

def presupuesto(request, pk):
	proyecto = Proyecto.objects.get(pk = pk)
	
	rubros = TipoRubro.objects.all()

	fuentes = Fuente.objects.filter(proyecto = proyecto)
	
	entidadProyecto = EntidadVsProyecto.objects.filter(proyecto = proyecto)

	pagos_array = []
	entidades_proyecto = []
	totales = []
	for fuente in fuentes:
		total = fuente.especie + fuente.efectivo
		totales.append(total)
		entidadVsProyecto = EntidadVsProyecto.objects.filter(entidad = fuente.entidad)
		entidades_proyecto.append(entidadVsProyecto)

	pagos = PagosProyecto.objects.filter(proyecto = proyecto)

		

	return render_to_response('base.html', {'proyecto':proyecto, 'fuentes': fuentes, 'rubros':rubros, 'entidadProyecto':entidadProyecto, 'totales':totales, 'pagos':pagos}, context_instance = RequestContext(request))

def rubroDetalle(request, pk, proyecto):

	#traer todos los pagos

	pagos = PagosProyecto.objects.filter(tipo_rubro = pk, proyecto = proyecto).order_by('entidad')
	rubro = TipoRubro.objects.get(pk = pk)
	print pagos

	return render_to_response('base_rubroDetalle.html', {'pagos':pagos, 'rubro':rubro, 'proyecto':proyecto}, context_instance = RequestContext(request))

@csrf_exempt
def eliminarPagoRubro(request, pk):
	pago = PagosProyecto.objects.get(pk = pk)
	pago.delete()
	
	return HttpResponse(1);