from django.db import models
from TipoFormacion.models import TipoFormacion

# Create your models here.

class Formacion(models.Model):
	tipo_formacion = models.ForeignKey(TipoFormacion)
	descripcion = models.TextField()

	def __unicode__(self):
		return self.descripcion