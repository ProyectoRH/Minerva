from django.db import models
from Investigador.models import Investigador
from Proyecto.models import Proyecto
from TipoVinculacion.models import TipoVinculacion
# Create your models here.

class InvestigadorVsProyecto(models.Model):
	investigador = models.ForeignKey(Investigador)
	proyecto = models.ForeignKey(Proyecto)
	tipo_vinculacion = models.ForeignKey(TipoVinculacion)
	funcion = models.CharField(max_length=255)
	horas_semanas = models.IntegerField()
	meses = models.IntegerField()

	class Meta:
		verbose_name='Cargo'
		verbose_name_plural='Participantes del proyecto'
	def __unicode__(self):
		return self.funcion
