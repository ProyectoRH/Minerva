# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Gremio(models.Model):
	usuario = models.ForeignKey(User)

	nombre_gremio = models.CharField(max_length=255)
	direccion = models.TextField()
	nombre_presidente = models.CharField(max_length=255, blank=True, null=True)
	telefono_presidente = models.IntegerField(blank=True, null=True)
	email_presidente = models.CharField(max_length=255, blank=True, null=True)
	nombre_director = models.CharField(max_length=255, blank=True, null=True)
	telefono_director = models.IntegerField(blank=True, null=True)
	email_director = models.CharField(max_length=255, blank=True, null=True)

	def __unicode__(self):
		return self.nombre_gremio
		

class EmpresarioBenemerito(models.Model):
	perfil_gremio = models.ForeignKey(Gremio)

	TIPO = (
		('benemerito','Empresario Benemérito'),
		('anio', 'Empresario del año')
	)

	tipo_empresario = models.CharField(max_length=200, choices=TIPO)

	nombre_empresario = models.CharField(max_length=255)
	direccion_contacto = models.TextField(blank=True, null=True)
	ciudad = models.CharField(max_length=200, blank=True, null=True)
	edad = models.IntegerField(help_text='años', blank=True, null=True)
	telefono_celular = models.CharField(max_length=255, blank=True, null=True)
	email = models.CharField(max_length=255, blank=True, null=True)

	liderazgo = models.TextField(blank=True, null=True)
	gestion_empresarial = models.TextField(blank=True, null=True)
	emprendimiento = models.TextField(blank=True, null=True)

	def __unicode__(self):
		return self.nombre_empresario


class OrganizacionEmpresario(models.Model):
	empresario = models.ForeignKey(EmpresarioBenemerito)
	nombre_organizacion = models.CharField(max_length=255, blank=True, null=True)
	cargos = models.TextField(blank=True, null=True)
	fecha = models.CharField(max_length=255, blank=True, null=True)
	creacion = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.empresario.nombre_empresario

class AdjuntosEmpresario(models.Model):
	empresario = models.ForeignKey(EmpresarioBenemerito)
	tipo_adjunto = models.IntegerField()
	adjunto = models.FileField(upload_to="static/uploads_premioMerito/empresario/", blank=True, null=True)
	creacion = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "Adjunto Empresario Tipo %s - %s" % (self.tipo_adjunto, self.empresario.nombre_empresario)