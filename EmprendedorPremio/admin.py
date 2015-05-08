from django.contrib import admin
from .models import Emprendedor, EntidadEmprendedor, DistincionesEmprendedor, AdjuntosEmprendedor
# Register your models here.

class EmprendedorAdmin(admin.ModelAdmin):
	list_filter = ('empresa_existe',)

admin.site.register(Emprendedor, EmprendedorAdmin)
admin.site.register(EntidadEmprendedor)
admin.site.register(DistincionesEmprendedor)
admin.site.register(AdjuntosEmprendedor)
