from django.contrib import admin
from .models import Investigador, TipoInvestigador
# Register your models here.

class InvestigadorAdmin(admin.ModelAdmin):
	list_display = ('nombre1', 'nombre2', 'apellido1', 'apellido2', 'numero_documento',)
	search_fields = ('nombre1', 'nombre2', 'apellido1', 'apellido2', 'numero_documento',)

admin.site.register(Investigador, InvestigadorAdmin)
admin.site.register(TipoInvestigador)
