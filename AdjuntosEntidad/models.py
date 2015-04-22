from django.db import models
from Entidad.models import Entidad
# Create your models here.

class AdjuntoEntidadMerito(models.Model):
	entidad = models.ForeignKey(Entidad)
	tipo_adjunto = models.IntegerField(blank=True, null=True)
	adjunto = models.FileField(upload_to="static/uploads_premioMerito/empresa/", blank=True, null=True)
	fecha_subida = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "Adjunto de %s" % (self.entidad.razon_social)