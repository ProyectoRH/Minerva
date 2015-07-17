# -*- coding: utf-8 -*-
from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from django.http import HttpResponse
from datetime import date

from django.contrib import admin
from .models import *
from Distinciones.models import Distincion
# Register your models here.

class TrabajadoresAdmin(admin.StackedInline):
	model = Trabajadores
	extra = 1
	suit_classes = 'suit-tab suit-tab-trabajadores'

class DescripcionesAdmin(admin.StackedInline):
	model = Descripciones
	extra = 1
	suit_classes = 'suit-tab suit-tab-descripciones'	

class DistincionesAdmin(admin.TabularInline):
	model = Distincion

class MEmpresaInnovadoraAdmin(admin.StackedInline):
	model = MeritoEmpresaInnovadora
	extra = 1
	suit_classes = 'suit-tab suit-tab-meritoEI'

class MEmpresaResponsabilidadSocAdmin(admin.StackedInline):
	model = MeritoResponsabilidadSocial
	extra = 1
	suit_classes = 'suit-tab suit-tab-meritoRSE'

class EntidadAdmin(admin.ModelAdmin):
	exclude = ('digitador',)
	inlines = [TrabajadoresAdmin, DescripcionesAdmin, MEmpresaInnovadoraAdmin, MEmpresaResponsabilidadSocAdmin]
	list_display = ['nit','razon_social',]
	search_fields = ['nit','razon_social',]
	fieldsets = [
		(None, {
			'classes': ('suit-tab', 'suit-tab-general',),
			'fields': ['perfil_usuario', 'nit','razon_social','direccion','url_web','telefono','nota_seguimiento','email','departamento','municipio','corregimiento','facebook','twitter',]
		}),
	]
	suit_form_tabs = (('general', 'Entidad'), ('trabajadores', 'Trabajadores'), ('descripciones', 'Descripciones'), ('meritoEI','Mérito Empresa Innovadora'), ('meritoRSE','Mérito a la Responsabilidad Social Empresarial'))

	# def save_model(self, request, obj, form, change):
	# 	obj.perfil_usuario = request.user
	# 	obj.save()

	@property
	def media(self):
		media = super(EntidadAdmin, self).media
		js = ["js/testEntidades.js",]
		media.add_js(js)
		return media

admin.site.register(Entidad, EntidadAdmin)
admin.site.register(MeritoEmpresaInnovadora)
admin.site.register(MeritoResponsabilidadSocial)
admin.site.register(MeritoEmpresaSalud)
admin.site.register(MeritoEmpresaIndustrial)
admin.site.register(MeritoEsfExportModalidad)
admin.site.register(MeritoEsfuerzoExportador)
admin.site.register(MeritoEmpresaComercial)
admin.site.register(MeritoEmpresaServicio)
admin.site.register(PerfilEntidadMerito)
admin.site.register(RepresentanteLegal)
admin.site.register(ContactosEntidad)
admin.site.register(MeritoEmpresaAgroindustrial)
admin.site.register(TipoOrganizacion)
admin.site.register(ActividadEconomica)
admin.site.register(TamanoOrganizacion)
admin.site.register(AlcanceMercado)
admin.site.register(Competitividad)
admin.site.register(RazonesParticipacion)
admin.site.register(CanalRecepcion)
admin.site.register(Trabajadores)
admin.site.register(AdjuntosEntidad)


