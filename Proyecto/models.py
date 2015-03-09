# -*- coding: utf-8 -*-
from django.db import models
from redactor.fields import RedactorField
from smart_selects.db_fields import ChainedForeignKey 
from Departamento.models import Departamento
from Municipio.models import Municipio
from Corregimiento.models import Corregimiento
from TipoInvestigacion.models import TipoInvestigacion
from CategoriaColciencias.models import Categoria
from TipoProyecto.models import TipoProyecto
from EstadoSituacion.models import Estado
from django.contrib.auth.models import User
from GrupoInvestigacion.models import GrupoInvestigacion

# Create your models here.

class Proyecto(models.Model):
	codigo_interno_proyecto = models.CharField(max_length=50, blank=True)
	tipo_proyecto = models.ForeignKey(TipoProyecto, verbose_name= u'Tipo de proyecto')
	titulo = models.TextField(verbose_name=u'Título del proyecto')
	duracion = models.IntegerField(help_text='En meses')
	fecha_inicio = models.DateField(verbose_name=u'Fecha de inicio')
	tipo_investigacion = models.ForeignKey(TipoInvestigacion, verbose_name = u'Tipo de investigación')
	grupos_investigacion = models.ManyToManyField(GrupoInvestigacion, verbose_name=u'Grupos de investigación')
	categoria_colciencias = models.ForeignKey(Categoria, default=None, verbose_name=u'Categoría en Colciencias')
	linea_investigacion = models.TextField(verbose_name = u'Línea de investigación')
	resumen = RedactorField(verbose_name=u'Resumen', redactor_options={'lang': 'es'}, upload_to='static/uploads_proyectos', allow_file_upload=True, allow_image_upload=True)	
	palabras_clave = models.TextField()

	departamento = models.ForeignKey(Departamento)
	municipio = ChainedForeignKey(
        Municipio, 
        chained_field="departamento",
        chained_model_field="COD_DEPTO", 
        show_all=False, 
        auto_choose=True
    )

	corregimiento = ChainedForeignKey(
        Corregimiento, 
        chained_field="municipio",
        chained_model_field="COD_MPIO", 
        show_all=False, 
        auto_choose=True
    )

	#---------- Descripción del proyecto -------------#
	planteamiento_problema = RedactorField(verbose_name=u'Planteamiento del problema', redactor_options={'lang': 'es'}, upload_to='static/uploads_proyectos', allow_file_upload=True, allow_image_upload=True)	
	estado_arte = RedactorField(verbose_name=u'Estado del arte', redactor_options={'lang': 'es'}, upload_to='static/uploads_proyectos', allow_file_upload=True, allow_image_upload=True)
	objetivos = RedactorField(verbose_name=u'Objetivos', redactor_options={'lang': 'es'}, upload_to='static/uploads_proyectos', allow_file_upload=True, allow_image_upload=True)
	metodologia = RedactorField(verbose_name=u'Metodología', redactor_options={'lang': 'es'}, upload_to='static/uploads_proyectos', allow_file_upload=True, allow_image_upload=True)

	#resultados = models.ForeignKey() #resultados

	impacto_esperado = RedactorField(verbose_name=u'Impacto esperado', redactor_options={'lang': 'es'}, upload_to='static/uploads_proyectos', allow_file_upload=True, allow_image_upload=True)
	estado = models.ForeignKey(Estado)
	digitador = models.ForeignKey(User)

	def __unicode__(self):
		return self.titulo
