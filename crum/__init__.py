# Python
import contextlib
import threading

_thread_locals = threading.local()

__version__ = '0.5'

__all__ = ['get_current_request', 'get_current_user', 'impersonate']


@contextlib.contextmanager
def impersonate(user=None):
    """Temporarily impersonate the given user for audit trails."""
    try:
        current_user = get_current_user()
        set_current_user(user)
        yield user
    finally:
        set_current_user(current_user)


def get_current_request():
    """Return the request associated with the current thread."""
    return getattr(_thread_locals, 'request', None)


def set_current_request(request=None):
    """Update the request associated with the current thread."""
    _thread_locals.request = request
    # Clear the current user if also clearing the request.
    if not request:
        _thread_locals.user = None


def get_current_user():
    """Return the user associated with the current request thread."""
    return getattr(get_current_request(), 'user',
                   getattr(_thread_locals, 'user', None))


def set_current_user(user=None):
    """Update the user associated with the current request thread."""
    request = get_current_request()
    if request:
        request.user = user
    # Allow impersonate to work without a request.
    _thread_locals.user = user


class CurrentRequestUserMiddleware(object):
    """Middleware to capture the request and user from the current thread."""

    def process_request(self, request):
        set_current_request(request)

    def process_response(self, request, response):
        set_current_request(None)
        return response

    def process_exception(self, request, exception):
        set_current_request(None)
