# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import defaultfilters
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import Gremio, EmpresarioBenemerito, OrganizacionEmpresario, AdjuntosEmpresario
# Create your views here.

@csrf_exempt
def crearEmpresario(request):
	if request.method == 'POST':
		tipo_empresario = request.POST.get("tipo_empresario")
		nombre_empresario = request.POST.get("nombre_empresario")
		direccion_contacto = request.POST.get("direccion_empresario")
		ciudad = request.POST.get("ciudad_empresario")
		edad = request.POST.get("edad_empresario")
		try:
			edad = int(edad)
		except:
			edad = 0
		telefono_celular = request.POST.get("telefono_empresario")
		email = request.POST.get("email_empresario")

		liderazgo = request.POST.get("liderazgo")
		gestion_empresarial = request.POST.get("gestion_empresarial")
		emprendimiento = request.POST.get("emprendimiento")

		print request.POST

		gremio_usuario = Gremio.objects.get(usuario = request.user)
		print "gremio %s" % (gremio_usuario)

		empresario_benemerito = EmpresarioBenemerito(
			perfil_gremio = gremio_usuario,
			tipo_empresario = tipo_empresario,
			nombre_empresario = nombre_empresario,
			direccion_contacto = direccion_contacto,
			ciudad = ciudad,
			edad = edad,
			telefono_celular = telefono_celular,
			email = email,
			liderazgo = liderazgo,
			gestion_empresarial = gestion_empresarial,
			emprendimiento = emprendimiento
		)
		empresario_benemerito.save()			


		return HttpResponse("%s<>%s" % (empresario_benemerito.pk, empresario_benemerito.nombre_empresario))

@csrf_exempt
def getEmpresario(request):
	
	if request.method == 'POST':
		empresario_id = request.POST.get("empresario_id")

		empresario = EmpresarioBenemerito.objects.get(pk = empresario_id)

		empresario_organizacionesObj = OrganizacionEmpresario.objects.filter(empresario = empresario)
		empresario_organizacionesArr = []
		for organizacion in empresario_organizacionesObj:
			empresario_organizacionesArr.append("%s<>%s<>%s<>%s" % (organizacion.pk, organizacion.nombre_organizacion, organizacion.cargos, organizacion.fecha))
		# Para los adjuntos
		empresario_adjuntosObj = AdjuntosEmpresario.objects.filter(empresario = empresario)
		empresario_adjuntosArr = []
		for adjunto in empresario_adjuntosObj:
			empresario_adjuntosArr.append("%s<>%s" % (adjunto.tipo_adjunto, adjunto.adjunto))

		data = {}
		if empresario:
			data['nombres'] = empresario.nombre_empresario
			data['tipo'] = empresario.tipo_empresario
			data['direccion'] = empresario.direccion_contacto
			data['ciudad'] = empresario.ciudad
			data['edad'] = empresario.edad
			data['telefono'] = empresario.telefono_celular
			data['email'] = empresario.email
			data['liderazgo'] = empresario.liderazgo
			data['gestion_empresarial'] = empresario.gestion_empresarial
			data['emprendimiento'] = empresario.emprendimiento
			data['organizaciones'] = empresario_organizacionesArr
			data['adjuntos'] = empresario_adjuntosArr

		return JsonResponse(data)
		
@csrf_exempt
def actualizarEmpresario(request):
	if request.method == 'POST':
		pk_empresario = request.POST.get("id_Emp")
		tipo_empresario = request.POST.get("tipo_empresario")
		nombre_empresario = request.POST.get("nombre_empresario")
		direccion_contacto = request.POST.get("direccion_empresario")
		ciudad = request.POST.get("ciudad_empresario")
		edad = request.POST.get("edad_empresario")
		try:
			edad = int(edad)
		except:
			edad = 0
		telefono_celular = request.POST.get("telefono_empresario")
		email = request.POST.get("email_empresario")

		liderazgo = request.POST.get("liderazgo")
		gestion_empresarial = request.POST.get("gestion_empresarial")
		emprendimiento = request.POST.get("emprendimiento")

		
		gremio_usuario = Gremio.objects.get(usuario = request.user)
		
		empresario_update = EmpresarioBenemerito.objects.get(pk = pk_empresario)
		empresario_update.perfil_gremio = gremio_usuario
		empresario_update.tipo_empresario = tipo_empresario
		empresario_update.nombre_empresario = nombre_empresario
		empresario_update.direccion_contacto = direccion_contacto
		empresario_update.ciudad = ciudad
		empresario_update.edad = edad
		empresario_update.telefono_celular = telefono_celular
		empresario_update.email = email
		empresario_update.liderazgo = liderazgo
		empresario_update.gestion_empresarial = gestion_empresarial
		empresario_update.emprendimiento = emprendimiento

		empresario_update.save()

		return HttpResponse(1)

@csrf_exempt
def crearOrganizacion(request):
	if request.method == 'POST':
		nombre_organizacion = request.POST.get("nombreOrganizacion")
		cargos_organizacion = request.POST.get("cargosOrganizacion")
		fecha_organizacion = request.POST.get("fechaOrganizacion")
		empresario_id = request.POST.get("empresario_id")
		try:
			empresario_id = int(empresario_id)
		except:
			empresario_id = 0

		empresarioObj = EmpresarioBenemerito.objects.get(pk = empresario_id)

		organizacion = OrganizacionEmpresario(
			empresario = empresarioObj,
			nombre_organizacion = nombre_organizacion,
			cargos = cargos_organizacion,
			fecha = fecha_organizacion
		)
		organizacion.save()
		return HttpResponse(organizacion.pk)

@csrf_exempt
def eliminarOrganizacion(request):
	if request.method == 'POST':
		organizacion_id = request.POST.get("id")

		organizacion = OrganizacionEmpresario.objects.get(pk = organizacion_id)
		organizacion.delete()

		return HttpResponse(1)


@csrf_exempt
def crearAdjuntoEmpresario(request, tipo):

	if request.method == 'POST':
		empresario_id = request.POST.get("empresario_id")
		try:
			empresario_id = int(empresario_id)
		except:
			empresario_id = 0
		empresario_update = EmpresarioBenemerito.objects.get(pk = empresario_id)

		tipo = int(tipo)
		adjunto_update = AdjuntosEmpresario.objects.filter(empresario = empresario_update, tipo_adjunto = tipo)
		if len(adjunto_update) == 0:
			adjuntoEmpresario = AdjuntosEmpresario(empresario = empresario_update)
			adjuntoEmpresario.tipo_adjunto = tipo
			adjuntoEmpresario.adjunto = request.FILES.values()[0]
			adjuntoEmpresario.save()
		else:
			adjunto_update[0].empresario = empresario_update
			adjunto_update[0].tipo_adjunto = tipo
			adjunto_update[0].adjunto = request.FILES.values()[0]
			
			adjunto_update[0].save()
		
		return HttpResponse(1)

	else:
		return HttpResponse(0)

@csrf_exempt
def consultarAdjuntoEmpresario(request, tipo):
	if request.method == 'POST':
		empresarioId = request.POST.get("empId")
		try:
			empresarioId = int(empresarioId)
		except:
			empresarioId = 0
		response = ""
		empresario_update = EmpresarioBenemerito.objects.get(pk = empresarioId)
		tipo = int(tipo)
		adjuntos = AdjuntosEmpresario.objects.filter(empresario = empresario_update, tipo_adjunto = tipo)		
		if len(adjuntos) > 0:
			response = "%s" % (adjuntos[0].adjunto)

		return HttpResponse(response)
	else:
		return HttpResponse(0)