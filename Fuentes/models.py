from django.db import models
from Entidad.models import Entidad
from Proyecto.models import Proyecto

# Create your models here.

class EstadoFuente(models.Model):
	descripcion = models.CharField(max_length=255)

	def __unicode__(self):
		return self.descripcion

class TipoRubro(models.Model):
	descripcion = models.CharField(max_length=255)

	def __unicode__(self):
		return self.descripcion

class Fuente(models.Model):
	entidad = models.ForeignKey(Entidad)
	proyecto = models.ForeignKey(Proyecto)
	tipo_fuente = models.ForeignKey(TipoRubro)
	fecha_consignacion=models.DateField()
	efectivo = models.PositiveIntegerField()
	especie = models.PositiveIntegerField()
	estado = models.ForeignKey(EstadoFuente)

	class Meta:
		verbose_name_plural='Fuentes Financieras'
		verbose_name='Fuente'

	def __unicode__(self):
		return self.entidad.razon_social
