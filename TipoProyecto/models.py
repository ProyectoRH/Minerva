from django.db import models

# Create your models here.

class TipoProyecto(models.Model):
	descripcion = models.CharField(max_length=100)

	def __unicode__(self):
		return self.descripcion