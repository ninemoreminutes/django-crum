# Django
from django.dispatch import receiver

# Django-CRUM
from crum import get_current_request
from crum.signals import current_user_getter, current_user_setter


@receiver(current_user_getter)
def _get_current_user_always_raises_exception(sender, **kwargs):
    raise RuntimeError('this receiver always raises an exception')


@receiver(current_user_getter)
def _get_current_user_always_returns_invalid(sender, **kwargs):
    return []


@receiver(current_user_getter)
def _get_current_user_always_returns_false(sender, **kwargs):
    return False


@receiver(current_user_getter)
def _get_current_user_always_returns_list_with_false(sender, **kwargs):
    return [False]


@receiver(current_user_setter)
def _set_current_user_always_raises_exception(sender, **kwargs):
    raise RuntimeError('this receiver always raises an exception')


@receiver(current_user_getter)
def _get_current_user_from_drf_request(sender, **kwargs):
    request = get_current_request()
    drf_request = getattr(request, 'drf_request', None)
    return (getattr(drf_request, 'user', False), 0)
