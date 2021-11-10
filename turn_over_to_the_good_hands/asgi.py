"""
ASGI config for turn_over_to_the_good_hands project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'turn_over_to_the_good_hands.settings')

application = get_asgi_application()
