"""
WSGI config for jmt_foundation project.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jmt_foundation.settings')
application = get_wsgi_application()