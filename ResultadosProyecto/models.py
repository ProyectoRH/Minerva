from django.db import models
from Proyecto.models import Proyecto
# Create your models here.

class Categoria(models.Model):
	descripcion = models.TextField()

	def __unicode__(self):
		return self.descripcion

class Producto(models.Model):
	proyecto = models.ForeignKey(Proyecto)
	categoria = models.ForeignKey(Categoria)
	archivo = models.FileField(upload_to='static/uploads_proyectos/productos')
	fecha_creacion = models.DateField(auto_now_add=True)
	fecha_entrega = models.DateField()
	resultado = models.TextField()
	indicador = models.TextField()
	beneficiario = models.TextField()

	def __unicode__(self):
		return self.resultado