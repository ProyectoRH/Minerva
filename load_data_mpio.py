# Full path and name to your csv file
csv_filepathname="/opt/minervaenv/Minerva/municipios.csv"
# Full path to your django project directory
home="/opt/minervaenv/Minerva/Minerva"

import sys,os
sys.path.append(home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django
django.setup()

from Departamento.models import Departamento
from Municipio.models import Municipio


import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=';', quotechar='"')
def utf8_encode(val):
    try:
        tmp = val.decode('utf8')
    except:
        try:
            tmp = val.decode('latin1')
        except:
            tmp= val.decode('ascii', 'ignore')
            tmp = tmp.encode('utf8')    
    return tmp
for row in dataReader:
    
    depto = Municipio()
    depto.COD_DEPTO = Departamento.objects.get(pk=row[0])
    depto.COD_MPIO = row[1]
    depto.NOM_MPIO = row[2]
    
    print "%s - %s - %s" % (depto.COD_DEPTO,depto.COD_MPIO,depto.NOM_MPIO)
    depto.save()
