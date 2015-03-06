from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Entidad(models.Model):
	nit = models.CharField(primary_key=True, unique=True, null=False, max_length=100)
	razon_social = models.TextField()
	direccion = models.TextField()
	url_web = models.URLField(blank=True, null=True)
	telefono = models.CharField(max_length=100)
	nota_seguimiento = models.TextField(blank=True, null=True)
	email = models.CharField(max_length=255, blank=True, null=True)
	digitador = models.ForeignKey(User)

	def __unicode__(self):
		return self.razon_social

class ContactosEntidad(models.Model):
	entidad = models.ForeignKey(Entidad)
	nombre = models.CharField(max_length=255)
	email = models.CharField(max_length=255, blank=True, null=True)
	telefono = models.CharField(max_length=100, blank=True, null=True)
	celular = models.CharField(max_length=100, blank=True, null=True)

	def __unicode__(self):
		return self.nombre

