from django.contrib import admin
from .models import Emprendedor, EntidadEmprendedor, DistincionesEmprendedor, AdjuntosEmprendedor
# Register your models here.

admin.site.register(Emprendedor)
admin.site.register(EntidadEmprendedor)
admin.site.register(DistincionesEmprendedor)
admin.site.register(AdjuntosEmprendedor)