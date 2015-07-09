from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.util import unquote
from django.template import RequestContext
from django.contrib.auth.models import User
from Proyecto.models import Proyecto
from Fuentes.models import Fuente, TipoRubro
from PagosProyecto.models import PagosProyecto
from EntidadVsProyecto.models import EntidadVsProyecto
from Entidad.models import Entidad, RepresentanteLegal, ContactosEntidad, PerfilEntidadMerito, Trabajadores, Descripciones, MeritoEmpresaInnovadora, MeritoResponsabilidadSocial, MeritoEmpresaSalud, MeritoEmpresaIndustrial, MeritoEsfuerzoExportador, MeritoEmpresaComercial, MeritoEmpresaServicio, MeritoEmpresaAgroindustrial

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
	entidades_Emprendedores = EntidadEmprendedor.objects.all()
	distinciones_emprendedores = DistincionesEmprendedor.objects.all()
	adjuntos_emprendedores = AdjuntosEmprendedor.objects.all()

	return render(request, "adminPremio/listaPrincipal.html", {'emprendedores':emprendedores, 'entidadEmprendedores':entidades_Emprendedores, 'disticionesEmprendedores':distinciones_emprendedores, 'adjuntosEmprendedores':adjuntos_emprendedores})

@login_required(login_url='/usuarios/registroEntidad/')
def listarEmpresas(request):
	empresas = Entidad.objects.exclude(pk = "")
	perfiles_empresas = PerfilEntidadMerito.objects.all()
	trabajadores_empresas = Trabajadores.objects.all()
	descripciones_empresas = Descripciones.objects.all()
	representantes_empresas = RepresentanteLegal.objects.all()
	contactos_empresas = ContactosEntidad.objects.all()
	distinciones_empresas = Distincion.objects.all()
	adjuntos_empresas = AdjuntoEntidadMerito.objects.all()

	return render(request, "adminPremio/listaPrincipal.html", {'entidades':empresas, 'perfilEntidades':perfiles_empresas, 'trabajadoresEntidades':trabajadores_empresas, 'descripcionesEntidades':descripciones_empresas, 'representanteEntidades':representantes_empresas, 'contactoEntidades':contactos_empresas, 'adjuntosEntidades':adjuntos_empresas, 'distincionesEntidades':distinciones_empresas})

@login_required(login_url='/usuarios/registroEntidad/')
def listarGremios(request):
	gremios = Gremio.objects.all()
	empresariosBen_gremio = EmpresarioBenemerito.objects.filter(tipo_empresario = "benemerito")
	empresariosAnio_gremio = EmpresarioBenemerito.objects.filter(tipo_empresario = "anio")

	return render(request, "adminPremio/listaPrincipal.html", {'gremios':gremios, 'empresariosBenemerito':empresariosBen_gremio, 'empresariosAnio':empresariosAnio_gremio})

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
	entidad = Entidad.objects.get(perfil_usuario = User.objects.get(pk = pk))
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


	##### Para las categorias ############
	empresa_MeritoInnovadora = MeritoEmpresaInnovadora.objects.filter(entidad = entidad)
	empresa_MeritoResponsabilidadSocial = MeritoResponsabilidadSocial.objects.filter(entidad = entidad)
	empresa_MeritoEmpresaSalud = MeritoEmpresaSalud.objects.filter(entidad = entidad)
	empresa_MeritoEmpresaIndustrial = MeritoEmpresaIndustrial.objects.filter(entidad = entidad)
	empresa_MeritoEsfuerzoExportador = MeritoEsfuerzoExportador.objects.filter(entidad = entidad)
	empresa_MeritoEmpresaComercial = MeritoEmpresaComercial.objects.filter(entidad = entidad)
	empresa_MeritoEmpresaServicio = MeritoEmpresaServicio.objects.filter(entidad = entidad)
	empresa_MeritoEmpresaAgroindustrial = MeritoEmpresaAgroindustrial.objects.filter(entidad = entidad)
	######################################


	return render(request, "adminPremio/detallesEntidad.html", {'entidad':entidad, 'representante':representanteLegal, 'contacto':contactoEntidad, 'perfil':perfilEntidad, 'trabajadores':trabajadores, 'descripciones':descripciones, 'anio_1':anio_actual1, 'anio_2':anio_actual2, 'anio_3':anio_actual3, 'distinciones':distinciones, 'adjuntos':adjuntosEntidad, 'otrosAdjuntos':otrosAdjuntosEntidad, 'empresaMeritoInnovadora':empresa_MeritoInnovadora[0], 'empresaMeritoRSocial':empresa_MeritoResponsabilidadSocial[0], 'empresaSalud':empresa_MeritoEmpresaSalud[0], 'empresaIndustrial':empresa_MeritoEmpresaIndustrial[0], 'empresaEsfuerzoExpo':empresa_MeritoEsfuerzoExportador[0], 'empresaComercial':empresa_MeritoEmpresaComercial[0], 'empresaServicio':empresa_MeritoEmpresaServicio[0], 'empresaAgro':empresa_MeritoEmpresaAgroindustrial[0]})

@login_required(login_url='/usuarios/registroEntidad/')
def detallesGremio(request, pk):
	gremio = Gremio.objects.get(pk = pk)
	empresarios = EmpresarioBenemerito.objects.filter(perfil_gremio = gremio)
	organizaciones_empresarios = OrganizacionEmpresario.objects.filter(empresario__perfil_gremio = gremio)
	adjuntos_empresarios = AdjuntosEmpresario.objects.filter(empresario__perfil_gremio = gremio)

	return render(request, "adminPremio/detallesGremio.html", {'gremio':gremio, 'empresarios':empresarios, 'organizacionesEmpresarios':organizaciones_empresarios, 'adjuntosEmpresarios':adjuntos_empresarios})

@login_required(login_url='/usuarios/registroEntidad/')
def detalleEmpresarioGremio(request, pk):
	empresario = EmpresarioBenemerito.objects.get(pk = pk)
	organizacion = OrganizacionEmpresario.objects.filter(empresario = empresario)
	adjuntos = AdjuntosEmpresario.objects.filter(empresario = empresario)
	return render(request, "adminPremio/detallesEmpresario.html", {'empresario':empresario, 'organizaciones':organizacion, 'adjuntos':adjuntos})
