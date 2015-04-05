# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey
from Departamento.models import Departamento
from Municipio.models import Municipio
from Corregimiento.models import Corregimiento

# Create your models here.

class TipoOrganizacion(models.Model):
	descripcion = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.descripcion

class ActividadEconomica(models.Model):
	descripcion = models.CharField(max_length=100)

	def __unicode__(self):
		return self.descripcion

class TamanoOrganizacion(models.Model):
	descripcion = models.TextField()

	def __unicode__(self):
		return self.descripcion

class CategoriaParticipacion(models.Model):
	descripcion = models.CharField(max_length=255)

	def __unicode__(self):
		return self.descripcion

class AlcanceMercado(models.Model):
	descripcion = models.CharField(max_length=255)

	def __unicode__(self):
		return self.descripcion

class Competitividad(models.Model):
	descripcion = models.CharField(max_length=255)

	def __unicode__(self):
		return self.descripcion	

class RazonesParticipacion(models.Model):
	descripcion = models.CharField(max_length=255)

	def __unicode__(self):
		return self.descripcion	

class CanalRecepcion(models.Model):
	descripcion = models.CharField(max_length=255)

	def __unicode__(self):
		return self.descripcion		

class Entidad(models.Model):
	perfil_usuario = models.OneToOneField(User)
	nit = models.CharField(primary_key=True, unique=True, null=False, max_length=100)
	razon_social = models.TextField()
	direccion = models.TextField()
	url_web = models.URLField(blank=True, null=True)
	telefono = models.CharField(max_length=100)
	nota_seguimiento = models.TextField(blank=True, null=True)
	email = models.CharField(max_length=255, blank=True, null=True)
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
	fax = models.CharField(max_length=50, blank=True, null=True)
	facebook = models.CharField(max_length=255, blank=True, null=True)
	twitter = models.CharField(max_length=255, blank=True, null=True)
	def __unicode__(self):
		return self.razon_social

class PerfilEntidadMerito(models.Model):
	entidad = models.ForeignKey(Entidad)
	pbx = models.CharField(max_length=200, blank=True, null=True)
	anios_operacion = models.IntegerField(help_text='años', blank=True, null=True)

	#--- Tipo de organizacion ----
	tipo_organizacion = models.ForeignKey(TipoOrganizacion, blank=True, null=True)
	tipo_organizacion_otra = models.CharField(max_length=200, blank=True, help_text='Especifique otro tipo', null=True)

	#--- Actividad economica ----
	actividad_economica = models.ForeignKey(ActividadEconomica, blank=True, null=True)
	actividad_economica_otra = models.CharField(max_length=200, blank=True, help_text='Especifique otra', null=True)

	codigo_ciiu = models.CharField(max_length=100, blank=True, null=True)
	tamano_organizacion = models.ForeignKey(TamanoOrganizacion, blank=True, null=True)
	alcance_mercado = models.ManyToManyField(AlcanceMercado, blank=True, default=None, null=True)
	
	#--- Por qué el producto es competitivo ----
	competitividad = models.ManyToManyField(Competitividad, blank=True, default=None, null=True)
	competitividad_especifique = models.CharField(max_length=200, blank=True, help_text='Especifique', default=None, null=True)

	#--- Razon por la cual participa ----
	razones_participacion = models.ManyToManyField(RazonesParticipacion, blank=True, default=None, null=True)
	razones_participacion_especifique = models.CharField(max_length=200, blank=True, help_text='Especifique otro', default=None, null=True)
	
	#--- Medio por el cual se entero ----
	canal_recepcion = models.ManyToManyField(CanalRecepcion, blank=True, default=None, null=True)
	canal_recepcion_especifique = models.CharField(max_length=200, blank=True, help_text='Especifique otro', default=None, null=True)

	# ------ Valor de ventas por año -------
	anio_venta_1 = models.IntegerField(blank=True, default=None, null=True)
	anio_venta_2 = models.IntegerField(blank=True, default=None, null=True)
	anio_venta_3 = models.IntegerField(blank=True, default=None, null=True)

	#------ Sistema de gestión ----
	calidad = models.CharField(max_length=255, help_text='Especifique norma y año de especificación si lo tiene' ,blank=True, default=None, null=True)
	seguridad_industrial = models.CharField(max_length=255, help_text='Especifique norma y año de especificación si lo tiene' ,blank=True, default=None, null=True)
	ambiental = models.CharField(max_length=255, help_text='Especifique norma y año de especificación si lo tiene' ,blank=True, default=None, null=True)
	otro = models.CharField(max_length=255, help_text='Especifique norma y año de especificación si lo tiene' ,blank=True, default=None, null=True)
	implementacion = models.CharField(verbose_name=u'En implementación', max_length=255, help_text='Especifique el porcentaje de avance si lo tiene' ,blank=True, default=None, null=True)

	#------ Investigacion e innovacion
	departamento_idi = models.BooleanField(default=False)
	asesor_externo = models.BooleanField(default=False)
	asesor_externo_especifique = models.CharField(max_length=255, blank=True, null=True)
	firma_consultora = models.BooleanField(default=False)
	firma_consultora_especifique = models.CharField(max_length=255, blank=True, null=True)
	alianza = models.BooleanField(default=False)
	alianza_especifique = models.CharField(max_length=255, blank=True, null=True)
	no_aplica = models.BooleanField(default=False)
	patentes = models.BooleanField(default=False)
	patentes_descripcion = models.TextField(blank=True, null=True)

	#------ Categoría de participación ----
	CATEGORIAS = (
		('meritoEI','Mérito a la Empresa Innovadora'),
		('meritoRSE', 'Mérito a la Responsabilidad Social Empresarial'),
		('meritoES', 'Mérito a la Empresa de Salud'),
		('meritoEIM','Mérito a la Empresa Industrial-Manufacturera'),
		('meritoEE', 'Mérito al Esfuerzo Exportador'),
		('meritoEC','Mérito a la Empresa Comercial'),
		('meritoEDS', 'Mérito a la Empresa de Servicios'),
		('meritoEAA', 'Mérito a la Empresa Agroindustrial-Agropecuaria'),
	)
	categoria = models.CharField(max_length=255, verbose_name=u'Categoría de participación', choices=CATEGORIAS, default=None, blank=True, null=True)
	creacion = models.DateField(auto_now_add=True)
	# --------------------------------------
	def __unicode__(self):
		return self.entidad.razon_social

class Trabajadores(models.Model):
	entidad = models.OneToOneField(Entidad)
	trabajadores_directos = models.IntegerField()
	trabajadores_indirectos = models.IntegerField()
	trabajadores_tecnico = models.IntegerField()
	trabajadores_tecnologo = models.IntegerField()
	trabajadores_profesional = models.IntegerField()
	trabajadores_profesional_esp = models.IntegerField()
	trabajadores_maestria = models.IntegerField()
	trabajadores_doctorado = models.IntegerField()
	creacion = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.entidad.razon_social

class Descripciones(models.Model):
	entidad = models.OneToOneField(Entidad)
	descripcion_productos = models.TextField()
	proveedores_principales = models.TextField()
	clientes_principales = models.TextField()
	creacion = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.entidad.razon_social


class RepresentanteLegal(models.Model):
	entidad = models.OneToOneField(Entidad)
	nombres = models.CharField(max_length=200)
	cargo = models.CharField(max_length=200)
	ciudad = models.CharField(max_length=200)
	direccion = models.CharField(max_length=200)
	telefono = models.CharField(max_length=100, blank=True)
	celular = models.CharField(max_length=100, blank=True)
	email = models.CharField(max_length=200)
	creacion = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.nombres


class ContactosEntidad(models.Model):
	entidad = models.ForeignKey(Entidad)
	nombres = models.CharField(max_length=255)
	cargo = models.CharField(max_length=200)
	ciudad = models.CharField(max_length=200)
	direccion = models.CharField(max_length=200)
	telefono = models.CharField(max_length=100, blank=True)
	celular = models.CharField(max_length=100, blank=True)
	email = models.CharField(max_length=200)
	creacion = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.nombres

class MeritoEmpresaInnovadora(models.Model):
	entidad = models.ForeignKey(Entidad)
	descripcion_a = models.TextField(blank=True, null=True, default=None, verbose_name=u'Mencione las personas dedicadas a actividades de Investigación, Desarrollo e Innovación en la empresa. Especifique nombre, cargo, nivel de formación y tiempo de dedicación (Debe expresarse en horas/mes)')
	descripcion_b = models.TextField(blank=True, null=True, default=None, verbose_name=u'Enumere las actividades de formación, relacionadas con el desarrollo de competencias en materia de innovación, en las que ha participado el personal de la empresa en los últimos 3 años. Indique el nombre de la actividad de formación y el número de asistentes')
	descripcion_c = models.TextField(blank=True, null=True, default=None, verbose_name=u'Describa los productos y/o servicios innovadores lanzados al mercado por la empresa en los últimos 3 años. Especifique nombre, fecha de lanzamiento (en formato DD/MM/AAAA), alcance (Local, Nacional o Internacional) y las ventas del producto o servicio para el último año (Debe expresar los valores en pesos colombianos)')
	descripcion_d = models.TextField(blank=True, null=True, default=None, verbose_name=u'Indique el porcentaje de innovaciones en productos y/o servicios realizadas conjuntamente con empresas o instituciones externas (Entiéndase como el cociente entre el número de productos y/o servicios innovadores trabajados conjuntamente con empresas o instituciones externas y el número total de productos y/o servicios realizados multiplicado por 100)')
	descripcion_e = models.TextField(blank=True, null=True, default=None, verbose_name=u'Describa el producto y/o servicio innovador más destacado desarrollado por la empresa en los últimos 3 años. Mencione la ficha técnica del producto y/o servicio, sus ventajas tecnológicas y el valor agregado que aporta.')
	descripcion_f = models.TextField(blank=True, null=True, default=None, verbose_name=u'Mencione las innovaciones en los procesos implementados en la empresa en los últimos 3 años. Especifique nombre, fecha de implementación (en formato DD/MM/AAAA), beneficios que le ha generado a la empresa y la modalidad de desarrollo utilizada (Desarrollo propio o Desarrollo en Alianza con una empresa o institución externa)')
	descripcion_g = models.TextField(blank=True, null=True, default=None, verbose_name=u'Realice una descripción de las innovaciones en marketing desarrolladas en los últimos 3 años por la empresa (Entiéndase como innovación la modificación de cualquiera de las variables del marketing como: nueva presentación de un producto, nuevo método de distribución, nueva forma de aplicación de un producto ya conocido, nuevos medios de promoción de ventas, etc.).')
	descripcion_h = models.TextField(blank=True, null=True, default=None, verbose_name=u'Describa las innovaciones en la gestión o administración de la empresa en los últimos 3 años (Entiéndase como innovación a la adopción de nuevos sistemas de dirección estratégica, nuevos sistemas de gestión del conocimiento, nueva estructuración de bases de datos para la gestión, etc.).')
	descripcion_i = models.TextField(blank=True, null=True, default=None, verbose_name=u'Indique las ventas que provienen de los productos y/o servicios innovadores para los últimos 3 años. (Debe expresar los valores en pesos colombianos)')
	descripcion_j = models.TextField(blank=True, null=True, default=None, verbose_name=u'Indique el valor de los gastos y/o inversiones realizadas en I+D+i en los últimos 3 años (Debe expresar los valores en pesos colombianos).')
	creacion = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.entidad.razon_social

class MeritoResponsabilidadSocial(models.Model):
	entidad = models.ForeignKey(Entidad)
	descripcion_a = models.TextField(blank=True, null=True, default=None, verbose_name=u'De acuerdo al balance social de la empresa, describa las principales acciones realizadas en el último año orientadas al mejoramiento de la calidad de vida de la comunidad interna y externa, evidenciando iniciativas que atiendan problematicas sociales específicas.*')
	descripcion_b = models.TextField(blank=True, null=True, default=None, verbose_name=u'Describa las acciones de alto impacto con las cuales la empresa ha contribuido al mejoramiento del medio ambiente.*')
	descripcion_c = models.TextField(blank=True, null=True, default=None, verbose_name=u'Describa las acciones de responsabilidad social implementadas por la empresa para con los empleados (aporte indicadores y alcances)*')
	descripcion_d = models.TextField(blank=True, null=True, default=None, verbose_name=u'Describa las acciones de responsabilidad social implementadas por la empresa para con los proveedores (aporte indicadores y alcances)*')
	descripcion_e = models.TextField(blank=True, null=True, default=None, verbose_name=u'Describa las acciones de responsabilidad social implementadas por la empresa para con la comunidad (aporte indicadores y alcances)*')
	creacion = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.entidad.razon_social

class MeritoEmpresaSalud(models.Model):
	entidad = models.ForeignKey(Entidad)
	descripcion_a = models.TextField(blank=True, null=True, default=None, verbose_name=u'Enumere y describa los proyectos generadores de productos y/o servicios innovadores en cuidado continuo que ha desarrollado la empresa en los últimos 3 años. (Monitoreo, Promoción, Prevención, Diagnóstico, Intervención).')
	descripcion_b = models.TextField(blank=True, null=True, default=None, verbose_name=u'Indique el número de usuarios atendidos con los productos y/o servicios innovadores enfocados en cuidado continuo en el último año.')
	descripcion_c = models.TextField(blank=True, null=True, default=None, verbose_name=u'Enumere y describa los productos y/o servicios diseñados que incorporen las TIC y su aplicación en el proceso de cuidado continuo.')
	descripcion_d = models.TextField(blank=True, null=True, default=None, verbose_name=u'¿Cuál ha sido la calificación obtenida en el último año en Servicio al Cliente?. Indique el tamaño de la población, el parámetro de calificación, el tamaño de la muestra y adjunte el instrumento utilizado.')
	creacion = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.entidad.razon_social

class MeritoEmpresaIndustrial(models.Model):
	entidad = models.ForeignKey(Entidad)
	descripcion_a = models.TextField(blank=True, null=True, default=None, verbose_name=u'Indique la productividad total de la empresa en los últimos 3 años (Entíendase productividad total como el cociente entre la producción total y los insumos totales por cien)')
	descripcion_b = models.TextField(blank=True, null=True, default=None, verbose_name=u'Describa la acciones de modernización tecnológica realizadas por la empresa en los últimos 3 años, indicando el nombre y la fecha de implementación (en formato DD/MM/AAAA).')
	descripcion_c = models.TextField(blank=True, null=True, default=None, verbose_name=u'Describa las acciones desarrolladas por la empresa para mitigar su impacto en el medio ambiente en los últimos 3 años, indique la fecha de implementación (en formato DD/MM/AAAA)')
	creacion = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.entidad.razon_social

class MeritoEsfExportModalidad(models.Model):
	descripcion = models.CharField(max_length=255)
	creacion = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.descripcion

class MeritoEsfuerzoExportador(models.Model):
	entidad = models.ForeignKey(Entidad)
	descripcion_a = models.IntegerField(blank=True, null=True, default=None, verbose_name=u'Mencione el año en el cual la empresa inició a exportar*')
	descripcion_b = models.IntegerField(blank=True, null=True, default=None, verbose_name=u'Indique el porcentaje de exportaciones de la empresa, de acuerdo a las ventas totales en el último año*')
	descripcion_c = models.TextField(blank=True, null=True, default=None, verbose_name=u'Mencione los paises con los cuales establece relaciones comerciales, especifique el porcentaje de exportaciones realizadas a cada país en el último año.*')
	descripcion_d = models.ManyToManyField(MeritoEsfExportModalidad ,verbose_name=u'Seleccione la modalidad de internacionalización que utiliza la empresa.')
	descripcion_d_otra = models.CharField(max_length=255, blank=True, verbose_name=u'Si otra, especifique')
	descripcion_e = models.TextField(blank=True, null=True, default=None, verbose_name=u'Indique el valor de las exportaciones y/o importaciones no tradicionales en el último año en valor FOB (Free On Board)* Entiéndase como valor FOB (Free On Board: Término de comercialización internacional que indica el precio de la mercancía a bordo de la nave o aeronave. Sin incluir fletes, seguros y otros gastos de manipulación después de embarcada la mercancía. El valor debe ser expresado en pesos colombianos - COP)')
	descripcion_f = models.TextField(blank=True, null=True, default=None, verbose_name=u'Describa los productos exportados en el último año y mencione el valor exportado en pesos colombianos - COP')
	descripcion_g = models.BooleanField(blank=True, verbose_name=u'Indique si la empresa importa materia prima para la fabricación de su producto', default=False)
	descripcion_h = models.IntegerField(blank=True, null=True, default=None, verbose_name=u'Si la respuesta a la pregunta anterior es afirmativa. Especifique el procentaje de materia prima importada en el producto final*')
	creacion = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.entidad.razon_social

class MeritoEmpresaComercial(models.Model):
	entidad = models.ForeignKey(Entidad)
	descripcion_a = models.TextField(blank=True, null=True, default=None, verbose_name=u' Mencione el número total de establecimientos comerciales que tiene la empresa actualmente.')
	descripcion_b = models.TextField(blank=True, null=True, default=None, verbose_name=u'Indique cuantos establecimientos comerciales ha abierto la empresa en los últimos 3 años, especifique donde están ubicados (domicilio, ciudad, país).')
	descripcion_c = models.TextField(blank=True, null=True, default=None, verbose_name=u'Describa los canales de comercialización utilizados para penetrar a nuevos mercados en los últimos 3 años, especificando ciudad y país.')
	descripcion_d = models.TextField(blank=True, null=True, default=None, verbose_name=u'Describa los productos y/o servicios nuevos dentro de la misma línea o lineas nuevas lanzadas al mercado en los últimos 3 años.')
	descripcion_e = models.TextField(blank=True, null=True, default=None, verbose_name=u'Describa las estrategias de comercialización novedosas, exitosas y comprobables utilizadas por la empresa en los últimos 3 años. Teniendo en cuenta modificaciones en las variables de marketing: producto, precio, distribución y promoción.')
	creacion = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.entidad.razon_social

class MeritoEmpresaServicio(models.Model):
	entidad = models.ForeignKey(Entidad)
	descripcion_a = models.TextField(blank=True, null=True, default=None, verbose_name=u'Describa los nuevos servicios y/o modelos innovadores en atención al cliente desarrollados por la empresa en los últimos 3 años.')	
	descripcion_b = models.TextField(blank=True, null=True, default=None, verbose_name=u'¿La empresa tiene un plan de formación y/o apoyo para el crecimiento profesional de sus empleados?. En caso afirmativo descríbalo.')
	descripcion_c = models.TextField(blank=True, null=True, default=None, verbose_name=u'Describa el plan de mejoramiento continuo de la empresa enfocado en servicio al cliente o sistemas de gestión implementados.')
	descripcion_d = models.TextField(blank=True, null=True, default=None, verbose_name=u'Mencione el número de personas capacitadas en servicio al cliente en el último año. Especifique las actividades de formación y fecha de realización de las mismas. (en formato DD/MM/AAAA).')
	descripcion_e = models.TextField(blank=True, null=True, default=None, verbose_name=u'Describa como la empresa ha implementado las TIC en sus servicios en los últimos 3 años.')
	descripcion_f = models.TextField(blank=True, null=True, default=None, verbose_name=u'¿Cuál ha sido la calificación obtenida por la empresa en el último año en Servicio al Cliente?. Indique el tamaño de la población, tamaño de la muestra, parámetro de calificación y adjunte el instrumento utilizado.')
	creacion = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.entidad.razon_social

class MeritoEmpresaAgroindustrial(models.Model):
	entidad = models.ForeignKey(Entidad)
	descripcion_a = models.TextField(blank=True, null=True, default=None, verbose_name=u'¿Cómo ha sido el comportamiento de la producción en su organización durante los últimos 5 años en términos de porcentaje (aumentos o disminuciones). Realice un breve comentario sobre los factores que han incidido en la producción.')
	descripcion_b = models.TextField(blank=True, null=True, default=None, verbose_name=u'Mencione los procesos tecnológicos implentemados en su organización que han permitido desarrollar nuevos productos y/o servicios en los últimos 5 años.')
	descripcion_c = models.TextField(blank=True, null=True, default=None, verbose_name=u'¿La organización ha desarrollado por su propia cuenta nuevas técnicas? Descríbalas y mencione los resultados obtenidos.')
	descripcion_d = models.TextField(blank=True, null=True, default=None, verbose_name=u'¿Cómo gestiona su organización la calidad de sus procesos? Especifique las certificaciones obtenidas y el año.')
	descripcion_e = models.TextField(blank=True, null=True, default=None, verbose_name=u'¿Cómo gestiona su organización la seguridad industrial y la salud ocupacional?')
	descripcion_f = models.TextField(blank=True, null=True, default=None, verbose_name=u'Describa las acciones encaminadas a la gestión ambiental que está ejecutando su organización tales como: manejos de residuos sólidos, de aguas servidas, cuencas hidrográficas, emisiones atmosféricas, desechos contaminantes, lixiviados polutantes, escapes de especies exóticas, eficiencia energética, uso racional de recursos hídricos y otros.')
	creacion = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.entidad.razon_social
