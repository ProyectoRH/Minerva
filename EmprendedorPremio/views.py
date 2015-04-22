# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import Emprendedor, EntidadEmprendedor, DistincionesEmprendedor, AdjuntosEmprendedor
from Entidad.models import TipoOrganizacion, ActividadEconomica, AlcanceMercado, CanalRecepcion
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import time
# Create your views here.

def guardarAdjuntos(request):
	return render(request, 'guardar-adjuntos.html', {})

@csrf_exempt
def crearEmprendedor(request):
	if request.method == 'POST':
		# ---- Card 1 ------
		nombres_emprendedor = request.POST.get("nombres_emprendedor")
		documento_emprendedor = request.POST.get("documento_emprendedor")
		genero = request.POST.get("genero")
		direccion_emprendedor = request.POST.get("direccion_emprendedor")
		telefono_emprendedor = request.POST.get("telefono_emprendedor")
		email_emprendedor = request.POST.get("email_emprendedor")
		email_corporativo = request.POST.get("email_corporativo")
		facebook_emprendedor = request.POST.get("facebook_emprendedor")
		# --- Card 2 ------
		empresa_labor_emp = request.POST.get("empresa_labor_emp")
		aEconomica_operacion = request.POST.get("aEconomica_operacion")
		actividad_economica_otra = request.POST.get("actividad_economica_otra")
		direccion_empresa_emp = request.POST.get("direccion_empresa_emp")
		telefonos_empresa_emp = request.POST.get("telefonos_empresa_emp")
		fax_empresa_emp = request.POST.get("fax_empresa_emp")
		web_empresa_emp = request.POST.get("web_empresa_emp")
		cargo_empresa_emp = request.POST.get("cargo_empresa_emp")
		ciudad_empresa_emp = request.POST.get("ciudad_empresa_emp")
		responsabilidades_empresa_emp = request.POST.get("responsabilidades_empresa_emp")
		jefe_empresa_emp = request.POST.get("jefe_empresa_emp")
		cargo_jefe_empresa_emp = request.POST.get("cargo_jefe_empresa_emp")
		telefono_jefe_empresa_emp = request.POST.get("telefono_jefe_empresa_emp")
		celular_jefe_empresa_emp = request.POST.get("celular_jefe_empresa_emp")
		correo_jefe_empresa_emp = request.POST.get("correo_jefe_empresa_emp")

		# ---- Card 3 ------
		estudios_pregrado_emp = request.POST.get("estudios_pregrado_emp")
		estudios_posgrado_emp = request.POST.get("estudios_posgrado_emp")
		convenio_practicas_emp = request.POST.get("convenio_practicas_emp")
		proyectos_emp = request.POST.get("proyectos_emp")
		asesoria_consultoria_emp = request.POST.get("asesoria_consultoria_emp")
		vinculacion_egresados_emp = request.POST.get("vinculacion_egresados_emp")
		relacion_otra_emp = request.POST.get("relacion_otra_emp")

		# ---- Card 4 -----
		perfil_profesional = request.POST.get("perfil_profesional")
		empresa_existe = request.POST.get("empresa_existe")
		try:
			empresa_existe = int(empresa_existe)
		except:
			empresa_existe = 0
		razon_social_emp = request.POST.get("razon_social_emp")
		nit_rut_emp = request.POST.get("nit_rut_emp")
		anios_operacion_emp = request.POST.get("anios_operacion_emp")
		try:
			anios_operacion_emp = int(anios_operacion_emp)
		except:
			anios_operacion_emp = 0
		
		empleoDirecto_trabajadores_emp = request.POST.get("empleoDirecto_trabajadores_emp")
		try:
			empleoDirecto_trabajadores_emp = int(empleoDirecto_trabajadores_emp)
		except:
			empleoDirecto_trabajadores_emp = 0
		empleoIndirecto_trabajadores_emp = request.POST.get("empleoIndirecto_trabajadores_emp")
		try:
			empleoIndirecto_trabajadores_emp = int(empleoIndirecto_trabajadores_emp)
		except:
			empleoIndirecto_trabajadores_emp = 0

		tOrganizacion_operacion_emp = request.POST.get("tOrganizacion_operacion_emp")
		tOrganizacionotra_operacion_emp = request.POST.get("tOrganizacionotra_operacion_emp")
		aEconomica_operacion_emp = request.POST.get("aEconomica_operacion_emp")
		aEconomicaOtra_operacion_emp = request.POST.get("aEconomicaOtra_operacion_emp")
		descripcion_proyecto_emp = request.POST.get("descripcion_proyecto_emp")
		descripcion_aporte_empresa_emp = request.POST.get("descripcion_aporte_empresa_emp")
		descripcion_impacto_emp = request.POST.get("descripcion_impacto_emp")

		# Para tipo de organizacion y actividad económica
		try:
			tipo_organizacion_operacion = TipoOrganizacion.objects.get(pk = tOrganizacion_operacion_emp)
		except:
			tipo_organizacion_operacion = None

		try:
			actividad_economica_operacion = ActividadEconomica.objects.get(pk = aEconomica_operacion)
		except:
			actividad_economica_operacion = None
		try:
			actividad_economica_operacionEmp = ActividadEconomica.objects.get(pk = aEconomica_operacion_emp)
		except:
			actividad_economica_operacionEmp = None
		
		canales_recepcion = request.POST.get("canal_recepcion_emp")
		canales_recepcionArr = canales_recepcion.split("-")
		canal_recepcionOtra = request.POST.get("canal_recepcionOtra_emp")

		emprendedor_update = Emprendedor.objects.filter(perfil_usuario = request.user)
		if len(emprendedor_update) > 0:
			entidad_emprendedor_update = EntidadEmprendedor.objects.filter(emprendedor = emprendedor_update[0])
	
		if len(emprendedor_update) == 0:
			print "a crear emprendedor"
			emprendedor = Emprendedor(
					perfil_usuario = request.user,
					nombres = nombres_emprendedor,
					documento = documento_emprendedor,
					genero = genero,
					direccion = direccion_emprendedor,
					telefono = telefono_emprendedor,
					correo_personal = email_emprendedor,
					correo_corporativo = email_corporativo,
					url_facebook = facebook_emprendedor,
					empresa_lab_actual = empresa_labor_emp,
					actividad_economica = actividad_economica_operacion,
					actividad_economica_otra = actividad_economica_otra,
					direccion_empresa = direccion_empresa_emp,
					telefonos_empresa = telefonos_empresa_emp,
					fax_empresa = fax_empresa_emp,
					web_empresa = web_empresa_emp,
					cargo_lab_empresa = cargo_empresa_emp,
					ciudad_lab_empresa = ciudad_empresa_emp,
					responsabilidades_empresa = responsabilidades_empresa_emp,
					jefe_inmediato_empresa = jefe_empresa_emp,
					cargo_jefe_empresa = cargo_jefe_empresa_emp,
					telefono_jefe_empresa = telefono_jefe_empresa_emp,
					celular_jefe_empresa = celular_jefe_empresa_emp,
					correo_jefe_empresa = correo_jefe_empresa_emp,
					estudios_pregrado = estudios_pregrado_emp,
					estudios_posgrado = estudios_posgrado_emp,
					convenio_practicas = convenio_practicas_emp,
					proyectos_investigacion = proyectos_emp,
					asesoria_consultoria = asesoria_consultoria_emp,
					vinculacion_laboral = vinculacion_egresados_emp,
					otra = relacion_otra_emp,
					empresa_existe = int(empresa_existe),
					perfil_profesional = perfil_profesional,
					canal_recepcion_otra = canal_recepcionOtra
				)
			emprendedor.save()
			emprendedor.canal_recepcion = {}
			for canal in canales_recepcionArr:
				if canal != "":
					canalObj = CanalRecepcion.objects.get(pk = canal)
					emprendedor.canal_recepcion.add(canalObj)

			print "emprendedor creado"
			entidadEmprendedor = EntidadEmprendedor(
					emprendedor = emprendedor,
					razon_social = razon_social_emp,
					nit_rut = nit_rut_emp,
					anios_operacion = anios_operacion_emp,
					trabajadores_directos = empleoDirecto_trabajadores_emp,
					trabajadores_indirectos = empleoIndirecto_trabajadores_emp,
					tipo_organizacion = tipo_organizacion_operacion,
					tipo_organizacion_otra = tOrganizacionotra_operacion_emp,
					actividad_economica = actividad_economica_operacionEmp,
					actividad_economica_otra = aEconomicaOtra_operacion_emp,
					descripcion_proyecto = descripcion_proyecto_emp,
					descripcion_aporte_empresa = descripcion_aporte_empresa_emp,
					descripcion_impacto = descripcion_impacto_emp
				)
			entidadEmprendedor.save()

			return HttpResponse(1)
		else:
			print "a actualizar emprendedor"
			emprendedor_update.update(
					perfil_usuario = request.user,
					nombres = nombres_emprendedor,
					documento = documento_emprendedor,
					genero = genero,
					direccion = direccion_emprendedor,
					telefono = telefono_emprendedor,
					correo_personal = email_emprendedor,
					correo_corporativo = email_corporativo,
					url_facebook = facebook_emprendedor,
					empresa_lab_actual = empresa_labor_emp,
					actividad_economica = actividad_economica_operacion,
					actividad_economica_otra = actividad_economica_otra,
					direccion_empresa = direccion_empresa_emp,
					telefonos_empresa = telefonos_empresa_emp,
					fax_empresa = fax_empresa_emp,
					web_empresa = web_empresa_emp,
					cargo_lab_empresa = cargo_empresa_emp,
					ciudad_lab_empresa = ciudad_empresa_emp,
					responsabilidades_empresa = responsabilidades_empresa_emp,
					jefe_inmediato_empresa = jefe_empresa_emp,
					cargo_jefe_empresa = cargo_jefe_empresa_emp,
					telefono_jefe_empresa = telefono_jefe_empresa_emp,
					celular_jefe_empresa = celular_jefe_empresa_emp,
					correo_jefe_empresa = correo_jefe_empresa_emp,
					estudios_pregrado = estudios_pregrado_emp,
					estudios_posgrado = estudios_posgrado_emp,
					convenio_practicas = convenio_practicas_emp,
					proyectos_investigacion = proyectos_emp,
					asesoria_consultoria = asesoria_consultoria_emp,
					vinculacion_laboral = vinculacion_egresados_emp,
					otra = relacion_otra_emp,
					empresa_existe = int(empresa_existe),
					perfil_profesional = perfil_profesional,
					canal_recepcion_otra = canal_recepcionOtra
				)
			print "si actualizo el perfil"
			emprendedor_update[0].canal_recepcion = {}
			for canal in canales_recepcionArr:
				if canal != "":
					canalObj = CanalRecepcion.objects.get(pk = canal)
					print canalObj
					emprendedor_update[0].canal_recepcion.add(canalObj)
			print "a actualizar emprendedor 2"
			if len(entidad_emprendedor_update) == 0:
				entidadEmprendedor = EntidadEmprendedor(
					emprendedor = emprendedor_update[0],
					razon_social = razon_social_emp,
					nit_rut = nit_rut_emp,
					anios_operacion = anios_operacion_emp,
					trabajadores_directos = empleoDirecto_trabajadores_emp,
					trabajadores_indirectos = empleoIndirecto_trabajadores_emp,
					tipo_organizacion = tipo_organizacion_operacion,
					tipo_organizacion_otra = tOrganizacionotra_operacion_emp,
					actividad_economica = actividad_economica_operacionEmp,
					actividad_economica_otra = aEconomicaOtra_operacion_emp,
					descripcion_proyecto = descripcion_proyecto_emp,
					descripcion_aporte_empresa = descripcion_aporte_empresa_emp,
					descripcion_impacto = descripcion_impacto_emp
				)
				entidadEmprendedor.save()
			else:
				entidad_emprendedor_update.update(
					emprendedor = emprendedor_update[0],
					razon_social = razon_social_emp,
					nit_rut = nit_rut_emp,
					anios_operacion = anios_operacion_emp,
					trabajadores_directos = empleoDirecto_trabajadores_emp,
					trabajadores_indirectos = empleoIndirecto_trabajadores_emp,
					tipo_organizacion = tipo_organizacion_operacion,
					tipo_organizacion_otra = tOrganizacionotra_operacion_emp,
					actividad_economica = actividad_economica_operacionEmp,
					actividad_economica_otra = aEconomicaOtra_operacion_emp,
					descripcion_proyecto = descripcion_proyecto_emp,
					descripcion_aporte_empresa = descripcion_aporte_empresa_emp,
					descripcion_impacto = descripcion_impacto_emp
				)
				

			return HttpResponse(2)
	else:
		return HttpResponse(0)

@csrf_exempt
def crearDistincion(request):
	anio_actual = time.strftime("%Y")
	if request.method == 'POST':
		distincion_reconocimiento = request.POST.get("reconocimiento")
		distincion_fecha = request.POST.get("fecha")
		distincion_alcances = request.POST.get("alcance")
		emprendedor_doc = request.POST.get("emprendedor_doc")

		emprendedor = Emprendedor.objects.filter(perfil_usuario = request.user, documento = emprendedor_doc)
		alcance = AlcanceMercado.objects.get(pk = distincion_alcances)

		distincion = DistincionesEmprendedor(
			emprendedor = emprendedor[0],
			reconocimiento = distincion_reconocimiento,
			fecha = distincion_fecha,
			alcance = alcance)
		distincion.save()
		
		return HttpResponse(distincion.pk)

@csrf_exempt
def eliminarDistincion(request):
	if request.method == 'POST':
		distincion_id = request.POST.get("id")

		distincion = DistincionesEmprendedor.objects.get(pk = distincion_id)
		distincion.delete()

		return HttpResponse(1)

@csrf_exempt
def crearAdjuntoEmprendedor(request, tipo):

	if request.method == 'POST':
		emprendedor_update = Emprendedor.objects.filter(perfil_usuario = request.user)
		tipo = int(tipo)
		adjunto_update = AdjuntosEmprendedor.objects.filter(emprendedor = emprendedor_update[0], tipo_adjunto = tipo)
		print request.FILES.values()
		if len(adjunto_update) == 0:
			print request.FILES
			adjuntoEmprendedor = AdjuntosEmprendedor(emprendedor = emprendedor_update[0])
			adjuntoEmprendedor.tipo_adjunto = tipo
			adjuntoEmprendedor.adjunto = request.FILES.values()[0]
			adjuntoEmprendedor.save()
		else:
			adjunto_update[0].emprendedor = emprendedor_update[0]
			adjunto_update[0].tipo_adjunto = tipo
			adjunto_update[0].adjunto = request.FILES.values()[0]
			adjunto_update[0].save()
			
		return HttpResponse(1)

	else:
		return HttpResponse(0)

@csrf_exempt
def consultarAdjuntoEmprendedor(request, tipo):
	if request.method == 'POST':
		emprendedor_update = Emprendedor.objects.filter(perfil_usuario = request.user)
		tipo = int(tipo)
		adjuntos = AdjuntosEmprendedor.objects.filter(emprendedor = emprendedor_update[0], tipo_adjunto = tipo)
		response = ""
		if len(adjuntos) > 0:
			response = "%s" % (adjuntos[0].adjunto)
		return HttpResponse(response)





