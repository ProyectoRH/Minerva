from django.contrib import admin
from .models import GrupoInvestigacion
# Register your models here.

class GruposAdmin(admin.ModelAdmin):
	filter_horizontal = ('investigadores',)

admin.site.register(GrupoInvestigacion, GruposAdmin)