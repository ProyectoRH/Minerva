# -*- coding: utf-8 -*-
from django.db import models
from Entidad.models import Entidad
from Proyecto.models import Proyecto
from Fuentes.models import TipoRubro
# Create your models here.

class TipoEjecucion(models.Model):
	descripcion = models.CharField(max_length=255)

	def __unicode__(self):
		return self.descripcion

class PagosProyecto(models.Model):
	proyecto = models.ForeignKey(Proyecto)
	entidad = models.ForeignKey(Entidad)
	tipo_rubro = models.ForeignKey(TipoRubro)
	numero_comprobante = models.IntegerField()
	fecha_solicitud = models.DateField()
	fecha_efectiva_pago = models.DateField()
	mer = models.IntegerField(help_text='Mes de ejecución del rubro')
	tipo_ejecucion = models.ForeignKey(TipoEjecucion)
	descripcion = models.TextField()
	valor = models.IntegerField()

	class Meta:
		verbose_name_plural='Pagos del proyecto'
		verbose_name='pago del proyecto con numero de comprobante'

	def __unicode__(self):
		return str(self.numero_comprobante)
	
class AdjuntoSolicitud(models.Model):
	pago = models.ForeignKey(PagosProyecto)
	archivo = models.FileField(upload_to='static/uploads_pagos')
	fecha_subida = models.DateField(auto_now_add=True)
	observacion = models.CharField(max_length=255)

	def __unicode__(self):
		return self.archivo.name


class AdjuntoEgreso(models.Model):
	pago = models.ForeignKey(PagosProyecto)
	archivo = models.FileField(upload_to='static/uploads_pagos')
	fecha_subida = models.DateField(auto_now_add=True)
	observacion = models.CharField(max_length=255)

	def __unicode__(self):
		return self.archivo.name
