#encoding:utf-8
"""
Django settings for Minerva project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$1=305&fgeuqx_d-mg1o0)3e3pf$d^&7r*c_ctf)e8b*(7&l@@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'redactor',
    'suit',
    'smart_selects',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'Departamento',
    'Municipio',
    'Corregimiento',
    'Proyecto',
    'TipoInvestigacion',
    'CategoriaColciencias',
    'Entidad',
    'Investigador',
    'TipoVinculacion',
    'InvestigadorVsProyecto',
    'EntidadVsProyecto',
    'Proveedores',
    'TipoProyecto',
    'AdjuntosProyecto',
    'Fuentes',
    'EstadoSituacion',
    'AdjuntosFuente',
    'Alertas',
    'PagosProyecto',
    'ResultadosProyecto',
    'GrupoInvestigacion',
    'Vistas',
    'Distinciones',
    'EmprendedorPremio',
    'EmpresarioBenemerito',
    'AdjuntosEntidad',
    'password_reset',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
#    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Minerva.urls'

WSGI_APPLICATION = 'Minerva.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'minerva20db',
        'USER': 'minervaus20',
        'PASSWORD': '?"i5=&{-a"3M',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-CO'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

#USE_DJANGO_JQUERY = False

#JQUERY_URL = "https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"

FILE_UPLOAD_MAX_MEMORY_SIZE = "214958080"

TEMPLATE_CONTEXT_PROCESSORS = TCP+( 
   'django.core.context_processors.request',
   'django.contrib.auth.context_processors.auth',
)

REDACTOR_OPTIONS = {'lang': 'es'}
REDACTOR_UPLOAD = '/static/uploads/'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['media'])
STATIC_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['content'])

STATICFILES_DIRS = (
   os.path.join(BASE_DIR, 'static'),
)

LOGIN_URL = '/usuarios/registroEntidad'

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'BILHA',
    # 'HEADER_DATE_FORMAT': 'l, j. F Y',
    # 'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    'CONFIRM_UNSAVED_CHANGES': False, # Default True

    # menu
    'SEARCH_URL': '/admin/Proyecto/proyecto/',
    # 'MENU_ICONS': {
    #    'sites': 'icon-leaf',
    #    'auth': 'icon-lock',
    # },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    # 'MENU': (
    #     'sites',
    #     {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
    #     {'app': 'proyecto', 'label': 'Proyectos', 'icon':'icon-list', 'models': ()},
    #     {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
    #     {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
    # ),

    # misc
    # 'LIST_PER_PAGE': 15
}

# if DEBUG:
#     EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
#     EMAIL_FILE_PATH = '/Users/juanpestana/Sites/Repositorios/MINERVA/Minerva/mensajes'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'juanpestana96@gmail.com'
EMAIL_HOST_PASSWORD = '8094885730'
DEFAULT_FROM_EMAIL = 'juanpestana96@gmail.com'
