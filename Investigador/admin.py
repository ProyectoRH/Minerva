from django.contrib import admin
from .models import Investigador, TipoInvestigador
# Register your models here.

class InvestigadorAdmin(admin.ModelAdmin):
	list_display = ('numero_documento',)
	search_fields = ('numero_documento',)

admin.site.register(Investigador, InvestigadorAdmin)
admin.site.register(TipoInvestigador)
