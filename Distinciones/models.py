# -*- coding: utf-8 -*-
from django.db import models
from Entidad.models import Entidad, AlcanceMercado
# Create your models here.

class Distincion(models.Model):
	entidad = models.ForeignKey(Entidad)
	reconocimiento = models.TextField(null=True, blank=True)
	fecha = models.DateField(null=True, blank=True)
	alcance = models.ForeignKey(AlcanceMercado, null=True, blank=True)
	creacion = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "%s - %s" % (self.entidad.razon_social, self.reconocimiento)