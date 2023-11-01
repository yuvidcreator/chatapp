"""
ASGI config for djangochannel project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
# from django.conf.urls import url
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochannel.settings')

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
import chat.routing


application = ProtocolTypeRouter({
    # "http": get_asgi_application(),
    # "websocket": AllowedHostsOriginValidator(AuthMiddlewareStack(
    #     URLRouter(
    #         chat.routing.websocket_urlpatterns
    #     )
    # )),
    "http": django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )
})