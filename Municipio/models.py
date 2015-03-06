from django.db import models
from Departamento.models import Departamento

class Municipio(models.Model):
    COD_DEPTO= models.ForeignKey(Departamento)
    COD_MPIO = models.CharField(max_length=100, primary_key=True)
    NOM_MPIO = models.CharField(max_length=255)
    def __unicode__(self):      
        return '%s - %s - (%s)' % (self.COD_MPIO,self.NOM_MPIO,self.COD_DEPTO.NOM_DEPTO)