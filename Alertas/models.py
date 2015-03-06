from django.db import models
from Proyecto.models import Proyecto

# Create your models here.

class EstadosAlerta(models.Model):
	descripcion = models.CharField(max_length=255)

	def __unicode__(self):
		return self.descripcion

class TipoAlerta(models.Model):
	descripcion = models.CharField(max_length=255)

	def __unicode__(self):
		return self.descripcion

class Alertas(models.Model):
	proyecto = models.ForeignKey(Proyecto)
	descripcion = models.TextField()
	fecha_creacion = models.DateField(auto_now_add=True)
	fecha_solicitud = models.DateTimeField()
	fecha_vencimiento = models.DateTimeField()
	estado = models.ForeignKey(EstadosAlerta)
	tipo_alerta = models.ForeignKey(TipoAlerta)

	class Meta:
		verbose_name='Alerta'
		verbose_name_plural='Alertas'

	def __unicode__(self):
		return self.descripcion
