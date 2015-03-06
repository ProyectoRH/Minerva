from django.contrib import admin
from Investigador.models import Investigador
from .models import InvestigadorVsProyecto
# Register your models here.

class InvestigadorVsProyectoAdmin(admin.ModelAdmin):
	raw_id_fields = ('investigador', )

admin.site.register(InvestigadorVsProyecto, InvestigadorVsProyectoAdmin)