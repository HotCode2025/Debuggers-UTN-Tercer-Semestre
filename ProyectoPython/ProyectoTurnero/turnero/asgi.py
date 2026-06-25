"""Aplicación ASGI para servidores con soporte asíncrono."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'turnero.settings')

application = get_asgi_application()
