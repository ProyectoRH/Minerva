from django.db import models
from Entidad.models import Entidad
# Create your models here.

class Descripciones(models.Model):
	entidad = models.ForeignKey(Entidad)
	descripcion_productos = models.TextField()
	proveedores_principales = models.TextField()
	clientes_principales = models.TextField()

	def __unicode__(self):
		return self.entidad