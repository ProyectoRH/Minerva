from django.db import models
from Entidad.models import Entidad
from Proyecto.models import Proyecto

# Create your models here.

class TipoParticipacion(models.Model):
	descripcion = models.TextField()
	def __unicode__(self):
		return self.descripcion

	def __unicode__(self):
		return self.descripcion

class EntidadVsProyecto(models.Model):
	entidad = models.ForeignKey(Entidad)
	proyecto = models.ForeignKey(Proyecto)
	tipo_participacion = models.ForeignKey(TipoParticipacion)

	class Meta:
		verbose_name = "Entidad"
		verbose_name_plural = "Entidades Participantes"

	def __unicode__(self):
		return self.entidad.razon_social
