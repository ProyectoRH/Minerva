# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from Entidad.models import ActividadEconomica, TipoOrganizacion, AlcanceMercado, CanalRecepcion
# Create your models here.

class Emprendedor(models.Model):
	perfil_usuario = models.OneToOneField(User)
	nombres = models.CharField(max_length=255, blank=True, null=True)
	documento = models.CharField(max_length=100, blank=True, null=True)
	GENEROS = (
		('masculino', 'Masculino'),
		('femenino', 'Femenino')
	)
	genero = models.CharField(max_length=100, choices=GENEROS, blank=True, null=True)
	direccion = models.CharField(max_length=255, blank=True, null=True)
	telefono = models.CharField(max_length=255, blank=True, null=True)
	correo_personal = models.CharField(max_length=255, blank=True, null=True)
	correo_corporativo = models.CharField(max_length=255, blank=True, null=True)
	url_facebook = models.CharField(max_length=255, blank=True, null=True)

	empresa_lab_actual = models.CharField(max_length=200, blank=True, null=True)
	actividad_economica = models.ForeignKey(ActividadEconomica, blank=True, null=True)
	actividad_economica_otra = models.CharField(max_length=255, blank=True, null=True)
	direccion_empresa = models.CharField(max_length=255, blank=True, null=True)
	telefonos_empresa = models.CharField(max_length=200, blank=True, null=True)
	fax_empresa = models.CharField(max_length=200, blank=True, null=True)
	web_empresa = models.CharField(max_length=200, blank=True, null=True)
	cargo_lab_empresa = models.CharField(max_length=200, blank=True, null=True)
	ciudad_lab_empresa = models.CharField(max_length=200, blank=True, null=True)
	responsabilidades_empresa = models.TextField(blank=True, null=True)
	jefe_inmediato_empresa = models.CharField(max_length=255, blank=True, null=True)
	cargo_jefe_empresa = models.CharField(max_length=255, blank=True, null=True)
	telefono_jefe_empresa = models.CharField(max_length=255, blank=True, null=True)
	celular_jefe_empresa = models.CharField(max_length=255, blank=True, null=True)
	correo_jefe_empresa = models.CharField(max_length=255, blank=True, null=True)

	estudios_pregrado = models.TextField(blank=True, null=True)
	estudios_posgrado = models.TextField(blank=True, null=True)
	convenio_practicas = models.CharField(max_length=255, blank=True, null=True)
	proyectos_investigacion = models.CharField(max_length=255, blank=True, null=True)
	asesoria_consultoria = models.CharField(max_length=255, blank=True, null=True)
	vinculacion_laboral = models.CharField(max_length=255, blank=True, null=True)
	otra = models.CharField(max_length=255, blank=True, null=True)

	empresa_existe = models.BooleanField(default=False)
	perfil_profesional = models.TextField(blank=True, null=True)

	canal_recepcion = models.ManyToManyField(CanalRecepcion, blank=True, null=True)
	canal_recepcion_otra = models.CharField(max_length=255, blank=True, null=True)

	def __unicode__(self):
		return self.nombres

class EntidadEmprendedor(models.Model):
	emprendedor = models.ForeignKey(Emprendedor)
	razon_social = models.CharField(max_length=255)
	nit_rut = models.CharField(max_length=255)
	anios_operacion = models.IntegerField(blank=True, null=True)

	trabajadores_directos = models.IntegerField(blank=True, null=True)
	trabajadores_indirectos = models.IntegerField(blank=True, null=True)

	tipo_organizacion = models.ForeignKey(TipoOrganizacion, blank=True, null=True)
	tipo_organizacion_otra = models.CharField(max_length=255, blank=True, null=True)

	actividad_economica = models.ForeignKey(ActividadEconomica, blank=True, null=True)
	actividad_economica_otra = models.CharField(max_length=255, blank=True, null=True)

	descripcion_proyecto = models.TextField(blank=True, null=True)
	descripcion_aporte_empresa = models.TextField(blank=True, null=True)
	descripcion_impacto = models.TextField(blank=True, null=True)

	def __unicode__(self):
		return "%s - %s" % (self.razon_social, self.emprendedor.nombres)


class DistincionesEmprendedor(models.Model):
	emprendedor = models.ForeignKey(Emprendedor)
	reconocimiento = models.CharField(max_length=255, null=True, blank=True)
	fecha = models.DateField(null=True, blank=True)
	alcance = models.ForeignKey(AlcanceMercado, null=True, blank=True)
	creacion = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "%s - %s" % (self.reconocimiento, self.emprendedor.nombres)

class AdjuntosEmprendedor(models.Model):
	emprendedor = models.ForeignKey(Emprendedor)
	tipo_adjunto = models.IntegerField()
	adjunto = models.FileField(upload_to="static/uploads_premioMerito/emprendedor/", blank=True, null=True)
	creacion = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "Archivo Adjunto Tipo %s - %s" %(str(self.tipo_adjunto), self.emprendedor.nombres)
