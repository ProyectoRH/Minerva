from django.contrib import admin
from .models import EmpresarioBenemerito, OrganizacionEmpresario, Gremio, AdjuntosEmpresario
# Register your models here.

admin.site.register(EmpresarioBenemerito)
admin.site.register(OrganizacionEmpresario)
admin.site.register(Gremio)
admin.site.register(AdjuntosEmpresario)