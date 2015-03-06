from django.db import models

# Create your models here.

class Proveedor(models.Model):
	nit = models.CharField(primary_key=True, unique=True, null=False, max_length=100)
	razon_social = models.TextField()
	descripcion = models.TextField()

	def __unicode__(self):
		return self.razon_social