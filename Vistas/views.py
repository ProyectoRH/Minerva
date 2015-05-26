from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from Proyecto.models import Proyecto
from Fuentes.models import Fuente, TipoRubro
from PagosProyecto.models import PagosProyecto
from EntidadVsProyecto.models import EntidadVsProyecto
from Entidad.models import Entidad, RepresentanteLegal, ContactosEntidad, PerfilEntidadMerito, Trabajadores, Descripciones

from EmprendedorPremio.models import Emprendedor, EntidadEmprendedor, DistincionesEmprendedor, AdjuntosEmprendedor
from Distinciones.models import Distincion

from AdjuntosEntidad.models import AdjuntoEntidadMerito

from EmpresarioBenemerito.models import Gremio, EmpresarioBenemerito, OrganizacionEmpresario, AdjuntosEmpresario

import time
from django.contrib.auth.decorators import login_required
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
	proyecto = Proyecto.objects.get(pk = proyecto)
	rubro = TipoRubro.objects.get(pk = pk)
	print pagos

	return render_to_response('base_rubroDetalle.html', {'pagos':pagos, 'rubro':rubro, 'proyecto':proyecto}, context_instance = RequestContext(request))

@csrf_exempt
def eliminarPagoRubro(request, pk):
	pago = PagosProyecto.objects.get(pk = pk)
	pago.delete()
	
	return HttpResponse(1);


# -------------- VISTAS PARA ADMIN DEL PREMIO ----------------------
@login_required(login_url='/usuarios/registroEntidad/')
def principalPremio(request):
	return render(request, "adminPremio/principal.html", {})

@login_required(login_url='/usuarios/registroEntidad/')
def listarEmprendedores(request):
	emprendedores = Emprendedor.objects.all()
	return render(request, "adminPremio/listaPrincipal.html", {'emprendedores':emprendedores})

@login_required(login_url='/usuarios/registroEntidad/')
def listarEmpresas(request):
	empresas = Entidad.objects.all()
	return render(request, "adminPremio/listaPrincipal.html", {'entidades':empresas})

@login_required(login_url='/usuarios/registroEntidad/')
def listarGremios(request):
	gremios = Gremio.objects.all()
	return render(request, "adminPremio/listaPrincipal.html", {'gremios':gremios})

@login_required(login_url='/usuarios/registroEntidad/')	
def detallesEmprendedor(request, pk):
	emprendedor = Emprendedor.objects.get(pk = pk)
	entidad_emprendedor = ""
	if emprendedor.empresa_existe == True:
		entidad_emprendedor = EntidadEmprendedor.objects.get(emprendedor = emprendedor)


	distincionesEmprendedor = DistincionesEmprendedor.objects.filter(emprendedor = emprendedor)

	adjuntosEmprendedor = AdjuntosEmprendedor.objects.filter(emprendedor = emprendedor)

	return render(request, "adminPremio/detallesEmprendedor.html", {'emprendedor':emprendedor, 'entidad':entidad_emprendedor, 'distinciones':distincionesEmprendedor, 'adjuntos':adjuntosEmprendedor})

@login_required(login_url='/usuarios/registroEntidad/')
def detallesEntidad(request, pk):
	entidad = Entidad.objects.get(pk = pk)
	representanteLegal = RepresentanteLegal.objects.get(entidad = entidad)
	contactoEntidad = ContactosEntidad.objects.get(entidad = entidad)
	perfilEntidad = PerfilEntidadMerito.objects.get(entidad = entidad)
	trabajadores = Trabajadores.objects.get(entidad = entidad)
	descripciones = Descripciones.objects.get(entidad = entidad)
	anio_actual = time.strftime("%Y")
	anio_actual1 = int(anio_actual) - 1
	anio_actual2 = int(anio_actual) - 2
	anio_actual3 = int(anio_actual) - 3

	distinciones = Distincion.objects.filter(entidad = entidad)
	adjuntosEntidad = AdjuntoEntidadMerito.objects.filter(entidad = entidad).exclude(tipo_adjunto = 10)
	otrosAdjuntosEntidad = AdjuntoEntidadMerito.objects.filter(entidad = entidad, tipo_adjunto = 10)


	return render(request, "adminPremio/detallesEntidad.html", {'entidad':entidad, 'representante':representanteLegal, 'contacto':contactoEntidad, 'perfil':perfilEntidad, 'trabajadores':trabajadores, 'descripciones':descripciones, 'anio_1':anio_actual1, 'anio_2':anio_actual2, 'anio_3':anio_actual3, 'distinciones':distinciones, 'adjuntos':adjuntosEntidad, 'otrosAdjuntos':otrosAdjuntosEntidad})

@login_required(login_url='/usuarios/registroEntidad/')
def detallesGremio(request, pk):
	gremio = Gremio.objects.get(pk = pk)
	empresarios = EmpresarioBenemerito.objects.filter(perfil_gremio = gremio)
	return render(request, "adminPremio/detallesGremio.html", {'gremio':gremio, 'empresarios':empresarios})

@login_required(login_url='/usuarios/registroEntidad/')
def detalleEmpresarioGremio(request, pk):
	empresario = EmpresarioBenemerito.objects.get(pk = pk)
	organizacion = OrganizacionEmpresario.objects.filter(empresario = empresario)
	adjuntos = AdjuntosEmpresario.objects.filter(empresario = empresario)
	return render(request, "adminPremio/detallesEmpresario.html", {'empresario':empresario, 'organizaciones':organizacion, 'adjuntos':adjuntos})
