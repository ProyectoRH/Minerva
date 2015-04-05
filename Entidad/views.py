# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *
from Departamento.models import Departamento
from Municipio.models import Municipio
from Corregimiento.models import Corregimiento
from datetime import datetime
from Distinciones.models import Distincion
import json
import time
# Create your views here.

def formularioRegistro(request):
	return render(request, 'formulario-registro.html', {})

def home(request):
	anio_actual = time.strftime("%Y")

	departamentos = Departamento.objects.all()
	actividades_economicas = ActividadEconomica.objects.all()
	tipos_organizacion = TipoOrganizacion.objects.all()
	tamanos_organizacion = TamanoOrganizacion.objects.all()

	alcance_mercado = AlcanceMercado.objects.all()
	competitividades = Competitividad.objects.all()
	razones_participacion = RazonesParticipacion.objects.all()
	canales_recepcion = CanalRecepcion.objects.all()

	modalidades_e_exportador = MeritoEsfExportModalidad.objects.all()
	entidad = ""
	if request.user.is_authenticated and request.user.is_active and request.user != "AnonymousUser":
		print request.user
		entidad = Entidad.objects.filter(perfil_usuario = request.user)

	representanteLegal_entidad = ""
	contacto_entidad = ""
	perfil_entidad_merito = ""
	trabajadores_entidad = ""
	descripciones_entidad = ""
	distinciones = []
	# Meritos
	meritoEI = ""
	meritoRSE = ""
	meritoES = ""
	meritoEIM = ""
	meritoEE = ""
	meritoEC = ""
	meritoEDS = ""
	meritoEAA = ""

	if len(entidad) > 0:
		representanteLegal_entidad = RepresentanteLegal.objects.filter(entidad = entidad[0])
		contacto_entidad = ContactosEntidad.objects.filter(entidad = entidad[0])
		perfil_entidad_merito = PerfilEntidadMerito.objects.filter(entidad = entidad[0])
		trabajadores_entidad = Trabajadores.objects.filter(entidad = entidad[0])
		descripciones_entidad = Descripciones.objects.filter(entidad = entidad[0])
		distinciones = Distincion.objects.filter(entidad = entidad[0]).order_by('pk')
		# Meritos
		meritoEI = MeritoEmpresaIndustrial.objects.filter(entidad = entidad[0])
		meritoRSE = MeritoResponsabilidadSocial.objects.filter(entidad = entidad[0])
		meritoES = MeritoEmpresaSalud.objects.filter(entidad = entidad[0])
		meritoEIM = MeritoEmpresaIndustrial.objects.filter(entidad = entidad[0])
		meritoEE = MeritoEsfuerzoExportador.objects.filter(entidad = entidad[0])
		meritoEC = MeritoEmpresaComercial.objects.filter(entidad = entidad[0])
		meritoEDS = MeritoEmpresaServicio.objects.filter(entidad = entidad[0])
		meritoEAA = MeritoEmpresaAgroindustrial.objects.filter(entidad = entidad[0])

	
	return render(request, 'inicio.html', {'departamentos':departamentos, 'actividades_eco':actividades_economicas, 'tipos_org':tipos_organizacion, 'entidad':entidad, 'perfil':perfil_entidad_merito, 'representante':representanteLegal_entidad, 'contacto':contacto_entidad, 'trabajadores':trabajadores_entidad, 'descripciones':descripciones_entidad, 'tamanos':tamanos_organizacion, 'alcances':alcance_mercado, 'competitividades':competitividades, 'razones':razones_participacion, 'canales':canales_recepcion, 'modalidadesEExportador':modalidades_e_exportador, 'merito_entidad_innovadora':meritoEI, 'merito_responsabilidad':meritoRSE, 'merito_empresa_salud':meritoES, 'merito_industrial':meritoEIM, 'merito_exportador':meritoEE, 'merito_empresa_comercial':meritoEC, 'merito_empresa_servicio':meritoEDS, 'merito_empresa_agro':meritoEAA, 'distinciones':distinciones})
	

@csrf_exempt
def registroPeticion(request):
	if request.method == 'POST':
		nombre = request.POST.get("nombre")
		apellido = request.POST.get("apellido")
		email = request.POST.get("email")
		password = request.POST.get("password")
			
		user_filter = User.objects.filter(email = email)
		if len(user_filter) == 0:
			user = User.objects.create_user(email, email, password)
			print user
			user.first_name = nombre
			user.last_name = apellido
			user.groups.add(Group.objects.get(name='ContactoPremio'))
			user.save()

			return HttpResponse(1)
			
		else:
			return HttpResponse(0)

@csrf_exempt
def iniciarSesionPeticion(request):
	if request.method == 'POST':
		usuario = request.POST.get("usuario")
		clave = request.POST.get("clave")
		
		user = authenticate(username=usuario, password=clave)
		print user
		if user is not None:
		    # the password verified for the user
		    if user.is_active:
		    	login(request, user)
		        return HttpResponse(1)
		    else:
		        return HttpResponse(0)
		else:
		    # the authentication system was unable to verify the username and password
		    return HttpResponse(0)

@csrf_exempt
def registrarEntidad(request):
	if request.method == 'POST':
		razon_social = request.POST.get("razon_social")
		nit_rut = request.POST.get("nit_rut")
		domicilio = request.POST.get("domicilio")
		
		departamento = request.POST.get("departamento")
		municipio = request.POST.get("municipio")
		corregimiento = request.POST.get("corregimiento")

		telefono = request.POST.get("telefono")
		fax = request.POST.get("fax")
		web = request.POST.get("web")
		email = request.POST.get("email")
		facebook = request.POST.get("facebook")
		twitter = request.POST.get("twitter")

		# ------- card Representante Legal --------
		nombre_repLegal = request.POST.get("nombre_repLegal")
		apellido_repLegal = request.POST.get("apellido_repLegal")
		cargo_repLegal = request.POST.get("cargo_repLegal")
		direccion_repLegal = request.POST.get("direccion_repLegal")
		ciudad_repLegal = request.POST.get("ciudad_repLegal")
		telefono_repLegal = request.POST.get("telefono_repLegal")
		celular_repLegal = request.POST.get("celular_repLegal")
		email_repLegal = request.POST.get("email_repLegal")

		# ------- card Contacto Entidad --------
		nombres_contacto = request.POST.get("nombres_contacto")
		cargo_contacto = request.POST.get("cargo_contacto")
		direccion_contacto = request.POST.get("direccion_contacto")
		ciudad_contacto = request.POST.get("ciudad_contacto")
		telefono_contacto = request.POST.get("telefono_contacto")
		celular_contacto = request.POST.get("celular_contacto")
		email_contacto = request.POST.get("email_contacto")

		# ------- card Operacion -------
		anios_operacion = request.POST.get("anios_operacion")
		try:
			anios_operacion = int(anios_operacion)
		except:
			anios_operacion = 0
		tOrganizacion_operacion = request.POST.get("tOrganizacion_operacion")
		tOrganizacionotra_operacion = request.POST.get("tOrganizacionotra_operacion")
		aEconomica_operacion = request.POST.get("aEconomica_operacion")
		aEconomicaOtra_operacion = request.POST.get("aEconomicaOtra_operacion")
		codigoCiuu_operacion = request.POST.get("codigoCiuu_operacion")

		# ------- card Organizacion -------

		empleoDirecto_trabajadores = request.POST.get("empleoDirecto_trabajadores")
		try:
			empleoDirecto_trabajadores = int(empleoDirecto_trabajadores)
		except:
			empleoDirecto_trabajadores = 0
		
		empleoIndirecto_trabajadores = request.POST.get("empleoIndirecto_trabajadores")
		try:
			empleoIndirecto_trabajadores = int(empleoIndirecto_trabajadores)
		except:
			empleoIndirecto_trabajadores = 0

		tecnicos_trabajadores = request.POST.get("tecnicos_trabajadores")
		try:
			tecnicos_trabajadores = int(tecnicos_trabajadores)
		except:
			tecnicos_trabajadores = 0

		tecnologos_trabajadores = request.POST.get("tecnologos_trabajadores")
		try:
			tecnologos_trabajadores = int(tecnologos_trabajadores)
		except:
			tecnologos_trabajadores = 0
		
		profesionales_trabajadores = request.POST.get("profesionales_trabajadores")
		try:
			profesionales_trabajadores = int(profesionales_trabajadores)
		except:
			profesionales_trabajadores = 0
		
		especializados_trabajadores = request.POST.get("especializados_trabajadores")
		try:
			especializados_trabajadores = int(especializados_trabajadores)
		except:
			especializados_trabajadores = 0

		maestrias_trabajadores = request.POST.get("maestrias_trabajadores")
		try:
			maestrias_trabajadores = int(maestrias_trabajadores)
		except:
			maestrias_trabajadores = 0
		
		doctores_trabajadores = request.POST.get("doctores_trabajadores")
		try:
			doctores_trabajadores = int(doctores_trabajadores)
		except:
			doctores_trabajadores = 0
		
		tamano_organizacion = request.POST.get("tamano_organizacion")

		# ------- card Mercado --------
		descProductos_mercado = request.POST.get("descProductos_mercado")
		descProveedores_mercado = request.POST.get("descProveedores_mercado")
		descClientes_mercado = request.POST.get("descClientes_mercado")
		anio_venta1 = request.POST.get("anio_venta_1")
		try:
			anio_venta1 = int(anio_venta1)
		except:
			anio_venta1 = 0
		anio_venta2 = request.POST.get("anio_venta_2")
		try:
			anio_venta2 = int(anio_venta2)
		except:
			anio_venta2 = 0
		anio_venta3 = request.POST.get("anio_venta_3")
		try:
			anio_venta3 = int(anio_venta3)
		except:
			anio_venta3 = 0
		alcance_mercado = request.POST.get("alcances")

		alcances_mercadoArr = alcance_mercado.split("-")

		# ------- card Sistema de Gestion --------
		calidad = request.POST.get("calidad")
		seguridad_industrial = request.POST.get("seguridad_industrial")
		ambiental = request.POST.get("ambiental")
		otro = request.POST.get("otro")
		implementacion = request.POST.get("implementacion")

		# ------- card Investigacion e innovacion
		departamento_idi = request.POST.get("departamento_idi")
		try:
			departamento_idi = int(departamento_idi)
		except:
			departamento_idi = 0
		
		asesor_externo = request.POST.get("asesor_externo")
		try:
			asesor_externo = int(asesor_externo)
		except:
			asesor_externo = 0
		asesor_externo_especifique = request.POST.get("asesor_externo_especifique")

		firma_consultora = request.POST.get("firma_consultora")
		try:
			firma_consultora = int(firma_consultora)
		except:
			firma_consultora = 0
		firma_consultora_especifique = request.POST.get("firma_consultora_especifique")

		alianza = request.POST.get("alianza")
		try:
			alianza = int(alianza)
		except:
			alianza = 0
		alianza_especifique = request.POST.get("alianza_especifique")
		
		no_aplica = request.POST.get("no_aplica")
		try:
			no_aplica = int(no_aplica)
		except:
			no_aplica = 0

		patentes = request.POST.get("patentes")
		try:
			patentes = int(patentes)
		except:
			patentes = 0
		patentes_descripcion = request.POST.get("patentes_descripcion")
		competitividad = request.POST.get("competitividad")

		competitividadArr = competitividad.split("-")
		competitividad_especifique = request.POST.get("competitividad_especifique")

		# ------- card Distinciones
		# Distincion 1
		reconocimiento1 = request.POST.get("reconocimiento1")
		fecha_distincion1 = request.POST.get("fecha_distincion1")
		alcance_distincion1 = request.POST.get("alcance_distincion1")
		# Distincion 2
		reconocimiento2 = request.POST.get("reconocimiento2")
		fecha_distincion2 = request.POST.get("fecha_distincion2")
		alcance_distincion2 = request.POST.get("alcance_distincion2")
		# Distincion 3
		reconocimiento3 = request.POST.get("reconocimiento3")
		fecha_distincion3 = request.POST.get("fecha_distincion3")
		alcance_distincion3 = request.POST.get("alcance_distincion3")
		# Distincion 4
		reconocimiento4 = request.POST.get("reconocimiento4")
		fecha_distincion4 = request.POST.get("fecha_distincion4")
		alcance_distincion4 = request.POST.get("alcance_distincion4")
		# Distincion 5
		reconocimiento5 = request.POST.get("reconocimiento5")
		fecha_distincion5 = request.POST.get("fecha_distincion5")
		alcance_distincion5 = request.POST.get("alcance_distincion5")
		# ------- card Participacion
		razones_participacion = request.POST.get("razones_participacion")
		razones_participacionArr = razones_participacion.split("-")
		razones_participacion_especifique = request.POST.get("razones_participacion_especifique")

		categoria_participacion = request.POST.get("categoria_participacion")

		canales_recepcion = request.POST.get("canales_recepcion")
		canales_recepcionArr = canales_recepcion.split("-")
		canal_recepcion_especifique = request.POST.get("canal_recepcion_especifique")

		# ------- card Detalles de la categoria
		# EMPRESA INNOVADORA
		meritoEI_a = request.POST.get("meritoEI_a")
		meritoEI_b = request.POST.get("meritoEI_b")
		meritoEI_c = request.POST.get("meritoEI_c")
		meritoEI_d = request.POST.get("meritoEI_d")
		meritoEI_e = request.POST.get("meritoEI_e")
		meritoEI_f = request.POST.get("meritoEI_f")
		meritoEI_g = request.POST.get("meritoEI_g")
		meritoEI_h = request.POST.get("meritoEI_h")
		meritoEI_i = request.POST.get("meritoEI_i")
		meritoEI_j = request.POST.get("meritoEI_j")
		# EMPRESA RESPONSABILIDAD SOCIAL
		meritoRSE_a = request.POST.get("meritoRSE_a")
		meritoRSE_b = request.POST.get("meritoRSE_b")
		meritoRSE_c = request.POST.get("meritoRSE_c")
		meritoRSE_d = request.POST.get("meritoRSE_d")
		meritoRSE_e = request.POST.get("meritoRSE_e")
		# EMPRESA DE SALUD
		meritoES_a = request.POST.get("meritoES_a")
		meritoES_b = request.POST.get("meritoES_b")
		meritoES_c = request.POST.get("meritoES_c")
		meritoES_d = request.POST.get("meritoES_d")
		# EMPRESA INDUSTRIAL-MANUFACTURERA
		meritoEIM_a = request.POST.get("meritoEIM_a")
		meritoEIM_b = request.POST.get("meritoEIM_b")
		meritoEIM_c = request.POST.get("meritoEIM_c")
		# ESFUERZO EXPORTADOR
		meritoEE_a = request.POST.get("meritoEE_a")
		meritoEE_b = request.POST.get("meritoEE_b")
		meritoEE_c = request.POST.get("meritoEE_c")
		meritoEE_d = request.POST.get("meritoEE_d")
		meritoEE_dArr = meritoEE_d.split("-")
		meritoEE_d_otra = request.POST.get("meritoEE_d_otra")
		meritoEE_e = request.POST.get("meritoEE_e")
		meritoEE_f = request.POST.get("meritoEE_f")
		meritoEE_g = request.POST.get("meritoEE_g")
		meritoEE_h = request.POST.get("meritoEE_h")
		# EMRPESA COMERCIAL
		meritoEC_a = request.POST.get("meritoEC_a")
		meritoEC_b = request.POST.get("meritoEC_b")
		meritoEC_c = request.POST.get("meritoEC_c")
		meritoEC_d = request.POST.get("meritoEC_d")
		meritoEC_e = request.POST.get("meritoEC_e")
		# EMPRESA DE SERVICIOS
		meritoEDS_a = request.POST.get("meritoEDS_a")
		meritoEDS_b = request.POST.get("meritoEDS_b")
		meritoEDS_c = request.POST.get("meritoEDS_c")
		meritoEDS_d = request.POST.get("meritoEDS_d")
		meritoEDS_e = request.POST.get("meritoEDS_e")
		meritoEDS_f = request.POST.get("meritoEDS_f")
		# EMPRESA AGROINDUSTRIAL-AGROPECUARIA
		meritoEAA_a =  request.POST.get("meritoEAA_a")
		meritoEAA_b =  request.POST.get("meritoEAA_b")
		meritoEAA_c =  request.POST.get("meritoEAA_c")
		meritoEAA_d =  request.POST.get("meritoEAA_d")
		meritoEAA_e =  request.POST.get("meritoEAA_e")
		meritoEAA_f =  request.POST.get("meritoEAA_f")

		# -------- Para departamento, municipio y corregimiento que vienen en POST ---
		if departamento:
			departamentoObj = Departamento.objects.get(pk = departamento)

		if  municipio:
			municipioObj = Municipio.objects.get(pk = municipio)

		if corregimiento:
			corregimientoObj = Corregimiento.objects.get(pk = corregimiento)
		# ----------------------------------------------------------------------------
		
		# -------- Para tipo de organizacion y para actividad economica que vienen en POST ---
		tipo_organizacion_operacion = TipoOrganizacion.objects.get(pk = tOrganizacion_operacion)
		actividad_economica_operacion = ActividadEconomica.objects.get(pk = aEconomica_operacion)
		# ------------------------------------------------------------------------------------

		# -------- Para tamano de la organizacion -------
		if tamano_organizacion:
			tamano_organizacionObj = TamanoOrganizacion.objects.get(pk = tamano_organizacion)
		else:
			tamano_organizacionObj = None
		entidad_update = Entidad.objects.filter(nit = nit_rut)
		entidad_users = Entidad.objects.filter(perfil_usuario = request.user)
		# ---- Objetos que deben ser traídos y consultados -------
		if len(entidad_update) > 0:
			representanteLegal_update = RepresentanteLegal.objects.filter(entidad = entidad_update[0])

			contacto_update = ContactosEntidad.objects.filter(entidad = entidad_update[0])

			perfil_merito = PerfilEntidadMerito.objects.filter(entidad = entidad_update[0])

			trabajadores_update = Trabajadores.objects.filter(entidad = entidad_update[0])

			descripciones_update = Descripciones.objects.filter(entidad = entidad_update[0])

		if len(entidad_update) == 0 or len(entidad_users) == 0:
			new_entidad = Entidad(perfil_usuario = request.user,nit = nit_rut,razon_social = razon_social,direccion = domicilio,url_web = web,telefono = telefono,nota_seguimiento = "",email = email,departamento = departamentoObj, municipio = municipioObj, corregimiento = corregimientoObj, facebook = facebook, twitter = twitter, fax = fax)
			new_entidad.save()
			print "entidad creada"
			new_RepresentanteLegal = RepresentanteLegal(
					entidad = new_entidad,
					nombres = nombre_repLegal,
					cargo = cargo_repLegal,
					ciudad = ciudad_repLegal,
					direccion = direccion_repLegal,
					telefono = telefono_repLegal,
					celular = celular_repLegal,
					email = email_repLegal)
			new_RepresentanteLegal.save()
			print "point - representante creado"
			new_Contacto = ContactosEntidad(
					entidad = new_entidad,
					nombres = nombres_contacto,
					cargo = cargo_contacto,
					ciudad = direccion_contacto,
					direccion = ciudad_contacto,
					telefono = telefono_contacto,
					celular = celular_contacto,
					email = email_contacto
				)
			new_Contacto.save()
			print "point - contacto creado"
			new_trabajadores = Trabajadores(
					entidad = new_entidad,
					trabajadores_directos = int(empleoDirecto_trabajadores),
					trabajadores_indirectos = int(empleoIndirecto_trabajadores),
					trabajadores_tecnico = int(tecnicos_trabajadores),
					trabajadores_tecnologo = int(tecnologos_trabajadores),
					trabajadores_profesional = int(profesionales_trabajadores),
					trabajadores_profesional_esp = int(especializados_trabajadores),
					trabajadores_maestria = int(maestrias_trabajadores),
					trabajadores_doctorado = int(doctores_trabajadores)
				)
			new_trabajadores.save()
			print "point - trabajadores creado"
			new_descripciones = Descripciones(
					entidad = new_entidad,
					descripcion_productos = descProductos_mercado,
					proveedores_principales = descProveedores_mercado,
					clientes_principales = descClientes_mercado
				)
			new_descripciones.save()
			print "point - descripciones creado"
			new_PerfilMeritoEmpresarial = PerfilEntidadMerito(
					entidad = new_entidad,
					anios_operacion = int(anios_operacion),
					tipo_organizacion = tipo_organizacion_operacion,
					tipo_organizacion_otra = tOrganizacionotra_operacion,
					actividad_economica = actividad_economica_operacion,
					actividad_economica_otra = aEconomicaOtra_operacion,
					codigo_ciiu = codigoCiuu_operacion,
					tamano_organizacion = tamano_organizacionObj,
					anio_venta_1 = anio_venta1,
					anio_venta_2 = anio_venta2,
					anio_venta_3 = anio_venta3,
					calidad = calidad,
					seguridad_industrial = seguridad_industrial,
					ambiental = ambiental,
					otro = otro,
					implementacion = implementacion,
					departamento_idi = int(departamento_idi),
					asesor_externo = int(asesor_externo),
					asesor_externo_especifique = asesor_externo_especifique,
					firma_consultora = int(firma_consultora),
					firma_consultora_especifique = firma_consultora_especifique,
					alianza = int(alianza),
					alianza_especifique = alianza_especifique,
					no_aplica = int(no_aplica),
					patentes = int(patentes),
					patentes_descripcion = patentes_descripcion,
					competitividad_especifique = competitividad_especifique,
					razones_participacion_especifique = razones_participacion_especifique,
					canal_recepcion_especifique = canal_recepcion_especifique,
					categoria = categoria_participacion
				)
			new_PerfilMeritoEmpresarial.save()

			new_PerfilMeritoEmpresarial.alcance_mercado = {}
			for alcance in alcances_mercadoArr:
				alcanceObj = AlcanceMercado.objects.get(pk = alcance)
				new_PerfilMeritoEmpresarial.alcance_mercado.add(alcanceObj)

			new_PerfilMeritoEmpresarial.competitividad = {}
			for competitividad in competitividadArr:
				competitividadObj = Competitividad.objects.get(pk = competitividad)
				new_PerfilMeritoEmpresarial.competitividad.add(competitividadObj)
			
			new_PerfilMeritoEmpresarial.razones_participacion = {}
			for razon in razones_participacionArr:
				razonObj = RazonesParticipacion.objects.get(pk = razon)
				new_PerfilMeritoEmpresarial.razones_participacion.add(razonObj)

			new_PerfilMeritoEmpresarial.canal_recepcion = {}
			for canal in canales_recepcionArr:
				canalObj = CanalRecepcion.objects.get(pk = canal)
				new_PerfilMeritoEmpresarial.canal_recepcion.add(canalObj)

			print "point - perfil creado"

			if categoria_participacion == "meritoEI":
				new_empresaInnovadora = MeritoEmpresaInnovadora(
					entidad = new_entidad,
					descripcion_a = meritoEI_a,
					descripcion_b = meritoEI_b,
					descripcion_c = meritoEI_c,
					descripcion_d = meritoEI_d,
					descripcion_e = meritoEI_e,
					descripcion_f = meritoEI_f,
					descripcion_g = meritoEI_g,
					descripcion_h = meritoEI_h,
					descripcion_i = meritoEI_i,
					descripcion_j = meritoEI_j 
				)
				new_empresaInnovadora.save()

			elif categoria_participacion == "meritoRSE":
				new_empresaResponsabilidad = MeritoResponsabilidadSocial(
					entidad = new_entidad,
					descripcion_a = meritoRSE_a,
					descripcion_b = meritoRSE_b,
					descripcion_c = meritoRSE_c,
					descripcion_d = meritoRSE_d,
					descripcion_e = meritoRSE_e
				)
				new_empresaResponsabilidad.save()
			
			elif categoria_participacion == "meritoES":
				new_empresaSalud = MeritoEmpresaSalud(
					entidad = new_entidad,
					descripcion_a = meritoES_a,
					descripcion_b = meritoES_b,
					descripcion_c = meritoES_c,
					descripcion_d = meritoES_d
				)
				new_empresaSalud.save()

			elif categoria_participacion == "meritoEIM":
				new_empresaIndustrial = MeritoEmpresaIndustrial(
					entidad = new_entidad,
					descripcion_a = meritoEIM_a,
					descripcion_b = meritoEIM_b,
					descripcion_c = meritoEIM_c
				)
				new_empresaIndustrial.save()

			elif categoria_participacion == "meritoEE":
				new_esfuerzoExportador = MeritoEsfuerzoExportador(
					entidad = new_entidad,
					descripcion_a = meritoEE_a,
					descripcion_b = meritoEE_b,
					descripcion_c = meritoEE_c,
					descripcion_d_otra = meritoEE_d_otra,
					descripcion_e = meritoEE_e,
					descripcion_f = meritoEE_f,
					descripcion_g = int(meritoEE_g),
					descripcion_h = meritoEE_h
				)
				new_esfuerzoExportador.save()
				new_esfuerzoExportador.descripcion_d = {}
				for modalidad in meritoEE_dArr:
					modalidadObj = MeritoEsfExportModalidad.objects.get(pk = modalidad)
					new_esfuerzoExportador.descripcion_d.add(modalidadObj)

			elif categoria_participacion == "meritoEC":
				new_empresaComercial = MeritoEmpresaComercial(
					entidad = new_entidad,
					descripcion_a = meritoEC_a,
					descripcion_b = meritoEC_b,
					descripcion_c = meritoEC_c,
					descripcion_d = meritoEC_d,
					descripcion_e = meritoEC_e
				)
				new_empresaComercial.save()

			elif categoria_participacion == "meritoEDS":
				new_empresaServicio = MeritoEmpresaServicio(
					entidad = new_entidad,
					descripcion_a = meritoEDS_a,
					descripcion_b = meritoEDS_b,
					descripcion_c = meritoEDS_c,
					descripcion_d = meritoEDS_d,
					descripcion_e = meritoEDS_e,
					descripcion_f = meritoEDS_f
				)
				new_empresaServicio.save()

			elif categoria_participacion == "meritoEAA":
				new_empresaAgro = MeritoEmpresaAgroindustrial(
					entidad = new_entidad,
					descripcion_a = meritoEAA_a,
					descripcion_b = meritoEAA_b,
					descripcion_c = meritoEAA_c,
					descripcion_d = meritoEAA_d,
					descripcion_e = meritoEAA_e,
					descripcion_f = meritoEAA_f
				)
				new_empresaAgro.save()

			# Para distincion 1
			if reconocimiento1 != "" and fecha_distincion1 != "" and alcance_distincion1 != "":
				alcanceObj1 = AlcanceMercado.objects.get(pk = alcance_distincion1)
				fecha = datetime.strptime(fecha_distincion1, "%Y-%m-%d")
				distincion1 = Distincion(entidad = new_entidad, reconocimiento = reconocimiento1, fecha = fecha, alcance = alcanceObj1)
				distincion1.save()
				print "distincion1 guardada"
			# Para distincion 2
			if reconocimiento2 != "" and fecha_distincion2 != "" and alcance_distincion2 != "":
				alcanceObj2 = AlcanceMercado.objects.get(pk = alcance_distincion2)
				distincion2 = Distincion(
					entidad = new_entidad,
					reconocimiento = reconocimiento2,
					fecha = fecha_distincion2,
					alcance = alcanceObj2
				)
				distincion2.save()

			# Para distincion 3
			if reconocimiento3 != "" and fecha_distincion3 != "" and alcance_distincion3 != "":
				alcanceObj3 = AlcanceMercado.objects.get(pk = alcance_distincion3)
				distincion3 = Distincion(
					entidad = new_entidad,
					reconocimiento = reconocimiento3,
					fecha = fecha_distincion3,
					alcance = alcanceObj3
				)
				distincion3.save()

			# Para distincion 4
			if reconocimiento4 != "" and fecha_distincion4 != "" and alcance_distincion4 != "":
				alcanceObj4 = AlcanceMercado.objects.get(pk = alcance_distincion4)
				distincion4 = Distincion(
					entidad = new_entidad,
					reconocimiento = reconocimiento4,
					fecha = fecha_distincion4,
					alcance = alcanceObj4
				)
				distincion4.save()

			# Para distincion 5
			if reconocimiento5 != "" and fecha_distincion5 != "" and alcance_distincion5 != "":
				alcanceObj5 = AlcanceMercado.objects.get(pk = alcance_distincion5)
				distincion5 = Distincion(
					entidad = new_entidad,
					reconocimiento = reconocimiento5,
					fecha = fecha_distincion5,
					alcance = alcanceObj5
				)
				distincion5.save()

			return HttpResponse(1)
		else:
			print "actualizar entidad"
			print departamentoObj
			print municipioObj
			entidad_update.update(perfil_usuario = request.user,nit = nit_rut,razon_social = razon_social,direccion = domicilio,url_web = web,telefono = telefono,nota_seguimiento = "",email = email,departamento = departamentoObj, municipio = municipioObj, corregimiento = corregimientoObj, facebook = facebook, twitter = twitter, fax = fax)

			print "entidad actualizada"
			if len(representanteLegal_update) == 0:
				new_RepresentanteLegal = RepresentanteLegal(
					entidad = entidad_update[0],
					nombres = nombre_repLegal,
					cargo = cargo_repLegal,
					ciudad = ciudad_repLegal,
					direccion = direccion_repLegal,
					telefono = telefono_repLegal,
					celular = celular_repLegal,
					email = email_repLegal)
				new_RepresentanteLegal.save()
			else:
				representanteLegal_update.update(
					entidad = entidad_update[0],
					nombres = nombre_repLegal,
					cargo = cargo_repLegal,
					ciudad = ciudad_repLegal,
					direccion = direccion_repLegal,
					telefono = telefono_repLegal,
					celular = celular_repLegal,
					email = email_repLegal)

			if len(contacto_update) == 0:
				new_Contacto = ContactosEntidad(
					entidad = entidad_update[0],
					nombres = nombres_contacto,
					cargo = cargo_contacto,
					ciudad = direccion_contacto,
					direccion = ciudad_contacto,
					telefono = telefono_contacto,
					celular = celular_contacto,
					email = email_contacto
				)
				new_Contacto.save()
			else:
				contacto_update.update(
					entidad = entidad_update[0],
					nombres = nombres_contacto,
					cargo = cargo_contacto,
					ciudad = direccion_contacto,
					direccion = ciudad_contacto,
					telefono = telefono_contacto,
					celular = celular_contacto,
					email = email_contacto)

			if len(perfil_merito) == 0:

				new_PerfilMeritoEmpresarial = PerfilEntidadMerito(
					entidad = entidad_update[0],
					anios_operacion = int(anios_operacion),
					tipo_organizacion = tipo_organizacion_operacion,
					tipo_organizacion_otra = tOrganizacionotra_operacion,
					actividad_economica = actividad_economica_operacion,
					actividad_economica_otra = aEconomicaOtra_operacion,
					codigo_ciiu = codigoCiuu_operacion,
					tamano_organizacion = tamano_organizacionObj,
					anio_venta_1 = anio_venta1,
					anio_venta_2 = anio_venta2,
					anio_venta_3 = anio_venta3,
					calidad = calidad,
					seguridad_industrial = seguridad_industrial,
					ambiental = ambiental,
					otro = otro,
					implementacion = implementacion,
					departamento_idi = int(departamento_idi),
					asesor_externo = int(asesor_externo),
					asesor_externo_especifique = asesor_externo_especifique,
					firma_consultora = int(firma_consultora),
					firma_consultora_especifique = firma_consultora_especifique,
					alianza = int(alianza),
					alianza_especifique = alianza_especifique,
					no_aplica = int(no_aplica),
					patentes = int(patentes),
					patentes_descripcion = patentes_descripcion,
					competitividad_especifique = competitividad_especifique,
					razones_participacion_especifique = razones_participacion_especifique,
					canal_recepcion_especifique = canal_recepcion_especifique,
					categoria = categoria_participacion)
				new_PerfilMeritoEmpresarial.save()
				
				new_PerfilMeritoEmpresarial.alcance_mercado = {}
				for alcance in alcances_mercadoArr:
					alcanceObj = AlcanceMercado.objects.get(pk = alcance)
					new_PerfilMeritoEmpresarial.alcance_mercado.add(alcanceObj)

				new_PerfilMeritoEmpresarial.competitividad = {}
				for competitividad in competitividadArr:
					competitividadObj = Competitividad.objects.get(pk = competitividad)
					new_PerfilMeritoEmpresarial.competitividad.add(competitividadObj)
				
				new_PerfilMeritoEmpresarial.razones_participacion = {}
				for razon in razones_participacionArr:
					razonObj = RazonesParticipacion.objects.get(pk = razon)
					new_PerfilMeritoEmpresarial.razones_participacion.add(razonObj)

				new_PerfilMeritoEmpresarial.canal_recepcion = {}
				for canal in canales_recepcionArr:
					canalObj = CanalRecepcion.objects.get(pk = canal)
					new_PerfilMeritoEmpresarial.canal_recepcion.add(canalObj)			

			else:				
				perfil_merito.update(
					entidad = entidad_update[0],
					anios_operacion = int(anios_operacion),
					tipo_organizacion = tipo_organizacion_operacion,
					tipo_organizacion_otra = tOrganizacionotra_operacion,
					actividad_economica = actividad_economica_operacion,
					actividad_economica_otra = aEconomicaOtra_operacion,
					codigo_ciiu = codigoCiuu_operacion,
					tamano_organizacion = tamano_organizacionObj,
					anio_venta_1 = anio_venta1,
					anio_venta_2 = anio_venta2,
					anio_venta_3 = anio_venta3,
					calidad = calidad,
					seguridad_industrial = seguridad_industrial,
					ambiental = ambiental,
					otro = otro,
					implementacion = implementacion,
					departamento_idi = int(departamento_idi),
					asesor_externo = int(asesor_externo),
					asesor_externo_especifique = asesor_externo_especifique,
					firma_consultora = int(firma_consultora),
					firma_consultora_especifique = firma_consultora_especifique,
					alianza = int(alianza),
					alianza_especifique = alianza_especifique,
					no_aplica = int(no_aplica),
					patentes = int(patentes),
					patentes_descripcion = patentes_descripcion,
					competitividad_especifique = competitividad_especifique,
					razones_participacion_especifique = razones_participacion_especifique,
					canal_recepcion_especifique = canal_recepcion_especifique,
					categoria = categoria_participacion
				)
				perfil_merito[0].alcance_mercado = {}
				for alcance in alcances_mercadoArr:
					alcanceObj = AlcanceMercado.objects.get(pk = alcance)
					perfil_merito[0].alcance_mercado.add(alcanceObj)

				perfil_merito[0].competitividad = {}
				for competitividad in competitividadArr:
					competitividadObj = Competitividad.objects.get(pk = competitividad)
					perfil_merito[0].competitividad.add(competitividadObj)
				
				perfil_merito[0].razones_participacion = {}
				for razon in razones_participacionArr:
					razonObj = RazonesParticipacion.objects.get(pk = razon)
					perfil_merito[0].razones_participacion.add(razonObj)

				perfil_merito[0].canal_recepcion = {}
				for canal in canales_recepcionArr:
					canalObj = CanalRecepcion.objects.get(pk = canal)
					perfil_merito[0].canal_recepcion.add(canalObj)

			if len(trabajadores_update) == 0:
				new_Trabajadores = Trabajadores(
					entidad = entidad_update[0],
					trabajadores_directos = int(empleoDirecto_trabajadores),
					trabajadores_indirectos = int(empleoIndirecto_trabajadores),
					trabajadores_tecnico = int(tecnicos_trabajadores),
					trabajadores_tecnologo = int(tecnologos_trabajadores),
					trabajadores_profesional = int(profesionales_trabajadores),
					trabajadores_profesional_esp = int(especializados_trabajadores),
					trabajadores_maestria = int(maestrias_trabajadores),
					trabajadores_doctorado = int(doctores_trabajadores)
				)
				new_Trabajadores.save()
			else:
				trabajadores_update.update(
					entidad = entidad_update[0],
					trabajadores_directos = int(empleoDirecto_trabajadores),
					trabajadores_indirectos = int(empleoIndirecto_trabajadores),
					trabajadores_tecnico = int(tecnicos_trabajadores),
					trabajadores_tecnologo = int(tecnologos_trabajadores),
					trabajadores_profesional = int(profesionales_trabajadores),
					trabajadores_profesional_esp = int(especializados_trabajadores),
					trabajadores_maestria = int(maestrias_trabajadores),
					trabajadores_doctorado = int(doctores_trabajadores)
				)

			if len(descripciones_update) == 0:
				new_Descripciones = Descripciones(
					entidad = entidad_update[0],
					descripcion_productos = descProductos_mercado,
					proveedores_principales = descProveedores_mercado,
					clientes_principales = descClientes_mercado
				)
				new_Descripciones.save()
			else:
				descripciones_update.update(
					entidad = entidad_update[0],
					descripcion_productos = descProductos_mercado,
					proveedores_principales = descProveedores_mercado,
					clientes_principales = descClientes_mercado
				)

			if categoria_participacion == "meritoEI":
				empresaInnovadora_update = MeritoEmpresaInnovadora.objects.filter(entidad = entidad_update[0])
				if len(empresaInnovadora_update) == 0:
					new_empresaInnovadora = MeritoEmpresaInnovadora(
						entidad = entidad_update[0],
						descripcion_a = meritoEI_a,
						descripcion_b = meritoEI_b,
						descripcion_c = meritoEI_c,
						descripcion_d = meritoEI_d,
						descripcion_e = meritoEI_e,
						descripcion_f = meritoEI_f,
						descripcion_g = meritoEI_g,
						descripcion_h = meritoEI_h,
						descripcion_i = meritoEI_i,
						descripcion_j = meritoEI_j 
					)
					new_empresaInnovadora.save()
				else:
					empresaInnovadora_update.update(
						entidad = entidad_update[0],
						descripcion_a = meritoEI_a,
						descripcion_b = meritoEI_b,
						descripcion_c = meritoEI_c,
						descripcion_d = meritoEI_d,
						descripcion_e = meritoEI_e,
						descripcion_f = meritoEI_f,
						descripcion_g = meritoEI_g,
						descripcion_h = meritoEI_h,
						descripcion_i = meritoEI_i,
						descripcion_j = meritoEI_j)

			elif categoria_participacion == "meritoRSE":
				empresaResponsabilidad_update = MeritoResponsabilidadSocial.objects.filter(entidad = entidad_update[0])
				if len(empresaResponsabilidad_update) == 0:
					new_empresaResponsabilidad = MeritoResponsabilidadSocial(
						entidad = entidad_update[0],
						descripcion_a = meritoRSE_a,
						descripcion_b = meritoRSE_b,
						descripcion_c = meritoRSE_c,
						descripcion_d = meritoRSE_d,
						descripcion_e = meritoRSE_e
					)
					new_empresaResponsabilidad.save()
				else:
					empresaResponsabilidad_update.update(
						entidad = entidad_update[0],
						descripcion_a = meritoRSE_a,
						descripcion_b = meritoRSE_b,
						descripcion_c = meritoRSE_c,
						descripcion_d = meritoRSE_d,
						descripcion_e = meritoRSE_e)
			
			elif categoria_participacion == "meritoES":
				empresaSalud_update = MeritoEmpresaSalud.objects.filter(entidad = entidad_update[0])
				if len(empresaSalud_update) == 0:
					new_empresaSalud = MeritoEmpresaSalud(
						entidad = entidad_update[0],
						descripcion_a = meritoES_a,
						descripcion_b = meritoES_b,
						descripcion_c = meritoES_c,
						descripcion_d = meritoES_d
					)
					new_empresaSalud.save()
				else:
					empresaSalud_update.update(
						entidad = entidad_update[0],
						descripcion_a = meritoES_a,
						descripcion_b = meritoES_b,
						descripcion_c = meritoES_c,
						descripcion_d = meritoES_d)

			elif categoria_participacion == "meritoEIM":
				empresaIndustrial_update = MeritoEmpresaIndustrial.objects.filter(entidad = entidad_update[0])
				if len(empresaIndustrial_update) == 0:
					new_empresaIndustrial = MeritoEmpresaIndustrial(
						entidad = entidad_update[0],
						descripcion_a = meritoEIM_a,
						descripcion_b = meritoEIM_b,
						descripcion_c = meritoEIM_c
					)
					new_empresaIndustrial.save()
				else:
					empresaIndustrial_update.update(
						entidad = entidad_update[0],
						descripcion_a = meritoEIM_a,
						descripcion_b = meritoEIM_b,
						descripcion_c = meritoEIM_c)

			elif categoria_participacion == "meritoEE":
				esfuerzoExportador_update = MeritoEsfuerzoExportador.objects.filter(entidad = entidad_update[0])
				if len(esfuerzoExportador_update) == 0:
					new_esfuerzoExportador = MeritoEsfuerzoExportador(
						entidad = entidad_update[0],
						descripcion_a = meritoEE_a,
						descripcion_b = meritoEE_b,
						descripcion_c = meritoEE_c,
						descripcion_d_otra = meritoEE_d_otra,
						descripcion_e = meritoEE_e,
						descripcion_f = meritoEE_f,
						descripcion_g = int(meritoEE_g),
						descripcion_h = meritoEE_h
					)
					new_esfuerzoExportador.save()
					new_esfuerzoExportador.descripcion_d = {}
					for modalidad in meritoEE_dArr:
						modalidadObj = MeritoEsfExportModalidad.objects.get(pk = modalidad)
						new_esfuerzoExportador.descripcion_d.add(modalidadObj)
				else:
					esfuerzoExportador_update.update(
						entidad = entidad_update[0],
						descripcion_a = meritoEE_a,
						descripcion_b = meritoEE_b,
						descripcion_c = meritoEE_c,
						descripcion_d_otra = meritoEE_d_otra,
						descripcion_e = meritoEE_e,
						descripcion_f = meritoEE_f,
						descripcion_g = int(meritoEE_g),
						descripcion_h = meritoEE_h)
					esfuerzoExportador_update[0].descripcion_d = {}
					for modalidad in meritoEE_dArr:
						modalidadObj = MeritoEsfExportModalidad.objects.get(pk = modalidad)
						esfuerzoExportador_update[0].descripcion_d.add(modalidadObj)

			elif categoria_participacion == "meritoEC":
				empresaComercial_update = MeritoEmpresaComercial.objects.filter(entidad = entidad_update[0])
				if len(empresaComercial_update) == 0:
					new_empresaComercial = MeritoEmpresaComercial(
						entidad = entidad_update[0],
						descripcion_a = meritoEC_a,
						descripcion_b = meritoEC_b,
						descripcion_c = meritoEC_c,
						descripcion_d = meritoEC_d,
						descripcion_e = meritoEC_e
					)
					new_empresaComercial.save()
				else:
					empresaComercial_update.update(
						entidad = entidad_update[0],
						descripcion_a = meritoEC_a,
						descripcion_b = meritoEC_b,
						descripcion_c = meritoEC_c,
						descripcion_d = meritoEC_d,
						descripcion_e = meritoEC_e)

			elif categoria_participacion == "meritoEDS":
				empresaServicio_update = MeritoEmpresaServicio.objects.filter(entidad = entidad_update[0])
				if len(empresaServicio_update) == 0:
					new_empresaServicio = MeritoEmpresaServicio(
						entidad = entidad_update[0],
						descripcion_a = meritoEDS_a,
						descripcion_b = meritoEDS_b,
						descripcion_c = meritoEDS_c,
						descripcion_d = meritoEDS_d,
						descripcion_e = meritoEDS_e,
						descripcion_f = meritoEDS_f
					)
					new_empresaServicio.save()
				else:
					empresaServicio_update.update(
						entidad = entidad_update[0],
						descripcion_a = meritoEDS_a,
						descripcion_b = meritoEDS_b,
						descripcion_c = meritoEDS_c,
						descripcion_d = meritoEDS_d,
						descripcion_e = meritoEDS_e,
						descripcion_f = meritoEDS_f)

			elif categoria_participacion == "meritoEAA":
				empresaAgro_update = MeritoEmpresaAgroindustrial.objects.filter(entidad = entidad_update[0])
				if len(empresaAgro_update) == 0:
					new_empresaAgro = MeritoEmpresaAgroindustrial(
						entidad = entidad_update[0],
						descripcion_a = meritoEAA_a,
						descripcion_b = meritoEAA_b,
						descripcion_c = meritoEAA_c,
						descripcion_d = meritoEAA_d,
						descripcion_e = meritoEAA_e,
						descripcion_f = meritoEAA_f
					)
					new_empresaAgro.save()
				else:
					empresaAgro_update.update(
						entidad = entidad_update[0],
						descripcion_a = meritoEAA_a,
						descripcion_b = meritoEAA_b,
						descripcion_c = meritoEAA_c,
						descripcion_d = meritoEAA_d,
						descripcion_e = meritoEAA_e,
						descripcion_f = meritoEAA_f)

			# Para distincion 1
			distinciones_update = Distincion.objects.filter(entidad = entidad_update[0])

			if reconocimiento1 != "" and fecha_distincion1 != "" and alcance_distincion1 != "":
				alcanceObj1 = AlcanceMercado.objects.get(pk = alcance_distincion1)
				distincion1 = Distincion(
					entidad = entidad_update[0],
					reconocimiento = reconocimiento1,
					fecha = fecha_distincion1,
					alcance = alcanceObj1
				)
				distincion1.save()

			# Para distincion 2
			if reconocimiento2 != "" and fecha_distincion2 != "" and alcance_distincion2 != "":
				alcanceObj2 = AlcanceMercado.objects.get(pk = alcance_distincion2)
				distincion2 = Distincion(
					entidad = entidad_update[0],
					reconocimiento = reconocimiento2,
					fecha = fecha_distincion2,
					alcance = alcanceObj2
				)
				distincion2.save()

			# Para distincion 3
			if reconocimiento3 != "" and fecha_distincion3 != "" and alcance_distincion3 != "":
				alcanceObj3 = AlcanceMercado.objects.get(pk = alcance_distincion3)
				distincion3 = Distincion(
					entidad = entidad_update[0],
					reconocimiento = reconocimiento3,
					fecha = fecha_distincion3,
					alcance = alcanceObj3
				)
				distincion3.save()

			# Para distincion 4
			if reconocimiento4 != "" and fecha_distincion4 != "" and alcance_distincion4 != "":
				alcanceObj4 = AlcanceMercado.objects.get(pk = alcance_distincion4)
				distincion4 = Distincion(
					entidad = entidad_update[0],
					reconocimiento = reconocimiento4,
					fecha = fecha_distincion4,
					alcance = alcanceObj4
				)
				distincion4.save()

			# Para distincion 5
			if reconocimiento5 != "" and fecha_distincion5 != "" and alcance_distincion5 != "":
				alcanceObj5 = AlcanceMercado.objects.get(pk = alcance_distincion5)
				distincion5 = Distincion(
					entidad = entidad_update[0],
					reconocimiento = reconocimiento5,
					fecha = fecha_distincion5,
					alcance = alcanceObj5
				)
				distincion5.save()

			return HttpResponse(2)
				
		

@csrf_exempt
def chainedMunicipio(request):
	if request.method == 'POST':
		departamento = request.POST.get("departamento")
		departamento = Departamento.objects.get(COD_DEPTO = departamento)

		municipios = Municipio.objects.filter(COD_DEPTO = departamento.COD_DEPTO)
		
		municipios_combo = []

		for municipio in municipios:
			municipios_dict = {}
			municipios_dict['COD_MPIO'] = municipio.COD_MPIO
			municipios_dict['NOM_MPIO'] = municipio.NOM_MPIO
			municipios_combo.append(municipios_dict)
			
		municipios_json = json.dumps(municipios_combo)

		return HttpResponse(municipios_json)

@csrf_exempt
def chainedCorregimiento(request):
	if request.method == 'POST':
		municipio = request.POST.get("municipio")
		municipio = Municipio.objects.get(COD_MPIO = municipio)


		corregimientos = Corregimiento.objects.filter(COD_MPIO = municipio.COD_MPIO)

		corregimientos_combo = []

		for corregimiento in corregimientos:
			corregimientos_dict = {}
			corregimientos_dict['COD_CORRE'] = corregimiento.COD_CORRE
			corregimientos_dict['NOM_CORRE'] = corregimiento.NOM_CORRE
			corregimientos_combo.append(corregimientos_dict)

		corregimientos_json = json.dumps(corregimientos_combo)

		return HttpResponse(corregimientos_json)

