from django.db import models
from Fuentes.models import Fuente
# Create your models here.

class EstadoAdjunto(models.Model):
	descripcion = models.CharField(max_length=255)

	def __unicode__(self):
		return self.descripcion

class AdjuntoFuente(models.Model):
	fuente = models.ForeignKey(Fuente)
	archivo = models.FileField(upload_to='static/uploads_fuentes')
	fecha_subida = models.DateField(auto_now_add=True)
	fecha_entrega = models.DateField()
	estado = models.ForeignKey(EstadoAdjunto)
	observacion = models.CharField(max_length=255)

	class Meta:
		verbose_name='Adjunto de una fuente o rubro'
		verbose_name_plural='Adjuntos de fuente o rubro'

	def __unicode__(self):
		return self.archivo.name