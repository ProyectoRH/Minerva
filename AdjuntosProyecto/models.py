# -*- encoding: utf-8 -*-
from django.db import models
from Proyecto.models import Proyecto
# Create your models here.

class EstadoAdjunto(models.Model):
	descripcion = models.CharField(max_length=255)

	def __unicode__(self):
		return self.descripcion

class TipoAdjunto(models.Model):
	descripcion = models.CharField(max_length=255)

	def __unicode__(self):
		return self.descripcion

class AdjuntoProyecto(models.Model):
	proyecto = models.ForeignKey(Proyecto)
	tipo_adjunto = models.ForeignKey(TipoAdjunto)
	archivo = models.FileField(upload_to='static/uploads_proyectos')
	fecha_subida = models.DateField(auto_now_add=True)
	fecha_entrega = models.DateField()
	estado = models.ForeignKey(EstadoAdjunto)
	observacion = models.CharField(max_length=255)

	class Meta:
		verbose_name='Adjunto del proyecto'
		verbose_name_plural='Adjuntos del proyecto'

	def __unicode__(self):
		return self.archivo.name