from django.db import models

# Create your models here.

class Estado(models.Model):
	descripcion = models.CharField(max_length=255)

	def __unicode__(self):
		return self.descripcion