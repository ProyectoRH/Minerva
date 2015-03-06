# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class TipoInvestigacion(models.Model):
	descripcion_tipo = models.CharField(max_length=255)

	def __unicode__(self):
		return self.descripcion_tipo