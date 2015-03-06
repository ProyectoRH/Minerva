from django.contrib import admin
from .models import EstadoAdjunto, TipoAdjunto, AdjuntoProyecto
# Register your models here.

admin.site.register(EstadoAdjunto)
admin.site.register(TipoAdjunto)
admin.site.register(AdjuntoProyecto)