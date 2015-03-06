from django.contrib import admin
from .models import Entidad
# Register your models here.

class EntidadAdmin(admin.ModelAdmin):
	exclude = ('digitador',)
	def save_model(self, request, obj, form, change):
		obj.digitador = request.user
		obj.save()

admin.site.register(Entidad, EntidadAdmin)