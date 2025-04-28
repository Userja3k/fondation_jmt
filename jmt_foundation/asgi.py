"""
ASGI config for jmt_foundation project.
"""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jmt_foundation.settings')
application = get_asgi_application()