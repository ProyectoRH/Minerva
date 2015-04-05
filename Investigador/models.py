# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TipoInvestigador(models.Model):
	descripcion = models.CharField(max_length=255)

	def __unicode__(self):
		return self.descripcion


class Investigador(models.Model):
	perfil_usuario = models.OneToOneField(User)
	numero_horas_investigacion = models.IntegerField(verbose_name="Horas de investigación", help_text='Por semana')
	numero_documento = models.CharField(verbose_name="Número de documento", max_length=45)
	tipo_investigador = models.ForeignKey(TipoInvestigador)

	class Meta:
		verbose_name='Persona'
		verbose_name_plural='Personas'

	def __unicode__(self):
		return self.numero_documento

