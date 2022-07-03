import os
import sys
 
sys.path.append('/home/v/vvbadmin/vvbrksi/public_html/vvb')
sys.path.append('/home/v/vvbadmin/myenv/lib/python3.6/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'vvb.settings'
import django
django.setup()
 
from django.core.handlers import wsgi
application = wsgi.WSGIHandler()
