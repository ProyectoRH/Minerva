from django.db import models

class Departamento(models.Model):
    COD_DEPTO = models.CharField(max_length=100, primary_key=True)
    NOM_DEPTO = models.CharField(max_length=255)
    def __unicode__(self):      
        return self.NOM_DEPTO
