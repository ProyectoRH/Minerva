from django.contrib import admin
from .models import Alertas, TipoAlerta, EstadosAlerta
# Register your models here.

admin.site.register(Alertas)
admin.site.register(TipoAlerta)
admin.site.register(EstadosAlerta)