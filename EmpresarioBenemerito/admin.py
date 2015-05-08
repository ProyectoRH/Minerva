from django.contrib import admin
from .models import EmpresarioBenemerito, OrganizacionEmpresario, Gremio, AdjuntosEmpresario
# Register your models here.


class EmpresarioAdmin(admin.ModelAdmin):
	list_filter = ('tipo_empresario',)
	class Meta:
		model = EmpresarioBenemerito
		verbose_name='Postulado'
		verbose_name_plural = 'Postulados'



admin.site.register(EmpresarioBenemerito, EmpresarioAdmin)
admin.site.register(OrganizacionEmpresario)
admin.site.register(Gremio)
admin.site.register(AdjuntosEmpresario)