from django.core.exceptions import PermissionDenied
from .models import Company


def user_is_authorized(function):
    def wrap(request, *args, **kwargs):
        if Company.objects.get(pk=kwargs['pk']).group in request.user.groups.all():
            return function(request, *args, **kwargs)
        elif request.user.is_staff or request.user.is_superuser:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
