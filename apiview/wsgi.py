"""
WSGI config for apiview project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
from decouple import config

from django.core.wsgi import get_wsgi_application

if config('MODE') == 'local':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apiview.settings.local')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apiview.settings.production')

application = get_wsgi_application()
