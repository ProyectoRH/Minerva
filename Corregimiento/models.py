from django.db import models
from Municipio.models import Municipio

class Corregimiento(models.Model):
    COD_MPIO= models.ForeignKey(Municipio)
    COD_CORRE = models.CharField(max_length=100, primary_key=True)
    NOM_CORRE = models.CharField(max_length=255)
    def __unicode__(self):      
        return '%s - %s - (%s)' % (self.COD_CORRE,self.NOM_CORRE,self.COD_MPIO.NOM_MPIO)
