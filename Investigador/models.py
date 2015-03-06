# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TipoInvestigador(models.Model):
	descripcion = models.CharField(max_length=255)

	def __unicode__(self):
		return self.descripcion


class Investigador(models.Model):
	nombre1 = models.CharField(verbose_name="Nombre", max_length=150)
	nombre2 = models.CharField(verbose_name="Segundo Nombre", max_length=150)
	apellido1 = models.CharField(verbose_name="Apellido", max_length=150)
	apellido2 = models.CharField(verbose_name="Segundo Apellido", max_length=150)
	numero_horas_investigacion = models.IntegerField(verbose_name="Horas de investigación", help_text='Por semana')
	numero_documento = models.CharField(verbose_name="Número de documento", max_length=200)
	tipo_investigador = models.ForeignKey(TipoInvestigador)

	class Meta:
		verbose_name='Persona'
		verbose_name_plural='Personas'

	def __unicode__(self):
		return '%s %s %s %s' % (self.nombre1, self.nombre2, self.apellido1, self.apellido2)

