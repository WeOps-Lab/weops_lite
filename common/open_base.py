from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet

from functools import wraps


def login_exempt(view_func):
    """"Mark a view function as being exempt from login view protection"""

    def wrapped_view(*args, **kwargs):
        return view_func(*args, **kwargs)

    wrapped_view.login_exempt = True
    return wraps(view_func)(wrapped_view)


class OpenAPIViewSet(ViewSet):
    permission_classes = [AllowAny]

    @classmethod
    def as_view(cls, actions=None, **kwargs):
        # 登录豁免
        view = super(ViewSet, cls).as_view(actions=actions, **kwargs)
        return csrf_exempt(login_exempt(view))
