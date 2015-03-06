from django.db import models
from Investigador.models import Investigador

# Create your models here.
class GrupoInvestigacion(models.Model):
	nombre = models.TextField()
	sigla = models.CharField(max_length=50)
	codigo_colombiano=models.CharField(max_length=50)
	investigadores = models.ManyToManyField(Investigador)

	class Meta:
		verbose_name_plural='Grupos'
		verbose_name='Grupo de investigacion'

	def __unicode__(self):
		return self.nombre
