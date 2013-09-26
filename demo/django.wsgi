import os
import sys

sys.path.append('/atlas/srv/glab/ison/gnowsys-studio/demo')
sys.path.append('/atlas/srv/glab/ison/gnowsys-studio')

os.environ['PYTHON_EGG_CACHE'] = '/atlas/srv/glab/ison/lib/python2.6/site-packages'
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()