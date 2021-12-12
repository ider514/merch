from django.core.wsgi import get_wsgi_application
import os
import sys

sys.path.append('/opt/bitnami/projects/merch')
os.environ.setdefault("PYTHON_EGG_CACHE",
                      "/opt/bitnami/projects/merch/egg_cache")


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'merch.settings.production')

application = get_wsgi_application()
