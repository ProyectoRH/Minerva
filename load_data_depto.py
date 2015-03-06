# Full path and name to your csv file
csv_filepathname="/Users/juanpestana/Sites/Repositorios/MINERVA/Minerva/departamentos.csv"
# Full path to your django project directory
home="/Users/juanpestana/Sites/Repositorios/MINERVA/Minerva/Minerva"

import sys,os
sys.path.append(home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django
django.setup()

from Departamento.models import Departamento


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
    
    
    depto = Departamento()
    depto.COD_DEPTO = row[0]
    depto.NOM_DEPTO = utf8_encode(row[1])
    
    print "%s " % (depto.COD_DEPTO)
    depto.save()
