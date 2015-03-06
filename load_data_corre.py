# Full path and name to your csv file
csv_filepathname="/Users/juanpestana/Sites/Repositorios/MINERVA/Minerva/corregimientos.csv"
# Full path to your django project directory
home="/Users/juanpestana/Sites/Repositorios/MINERVA/Minerva/Minerva"

import sys,os
sys.path.append(home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django
django.setup()


from Municipio.models import Municipio
from Corregimiento.models import Corregimiento


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
    
    depto = Corregimiento()
    depto.COD_MPIO = Municipio.objects.get(pk=row[0])
    depto.COD_CORRE = row[1]
    depto.NOM_CORRE = row[2]
    
    print "%s - %s - %s" % (depto.COD_MPIO,depto.COD_CORRE,depto.NOM_CORRE)
    depto.save()
