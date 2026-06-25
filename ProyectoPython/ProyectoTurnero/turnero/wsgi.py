"""Aplicación WSGI para el despliegue tradicional de Django."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'turnero.settings')

application = get_wsgi_application()
