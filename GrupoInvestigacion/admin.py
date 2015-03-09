from django.contrib import admin
from .models import GrupoInvestigacion
# Register your models here.

class GruposAdmin(admin.ModelAdmin):
	filter_horizontal = ('investigadores',)
	list_display = ['nombre','sigla','codigo_colombiano',]
	search_fields = ['nombre','sigla','codigo_colombiano',]

admin.site.register(GrupoInvestigacion, GruposAdmin)