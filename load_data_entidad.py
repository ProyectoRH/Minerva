# Full path and name to your csv file
csv_filepathname="/Users/Sites/Repositorios/MINERVA/Minerva/entidades.csv"
# Full path to your django project directory
home="/Users/Sites/Repositorios/MINERVA/Minerva/Minerva"

import sys,os
sys.path.append(home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django
django.setup()


from Entidad.models import Entidad


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
    entidad = Entidad()
    entidad.nit = row[0]
    entidad.razon_social = row[1]
    entidad.direccion = row[2]
    entidad.url_web = row[3]
    entidad.telefono = row[4]
    entidad.email = row[5]
    
    print "%s - %s - %s - %s - %s" % (entidad.nit, entidad.razon_social, entidad.direccion, entidad.url_web, entidad.telefono, entidad.email)
    entidad.save()
