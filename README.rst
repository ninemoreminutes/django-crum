|Build Status| |PyPI Version| |PyPI License| |Python Versions| |Django Versions| |Read the Docs|

Django-CRUM
===========

Django-CRUM (Current Request User Middleware) captures the current request and
user in thread local storage.

It enables apps to check permissions, capture audit trails or otherwise access
the current request and user without requiring the request object to be passed
directly. It also offers a context manager to allow for temporarily
impersonating another user.

It provides a signal to extend the built-in function for getting the current
user, which could be helpful when using custom authentication methods or user
models.

Documentation can be found at `RTFD <http://django-crum.readthedocs.io/>`_.

It is tested against:
 * Django 2.2 (Python 3.8 and 3.9)
 * Django 3.0 (Python 3.8 and 3.9)
 * Django 3.1 (Python 3.8 and 3.9)
 * Django 3.2 (Python 3.8, 3.9 and 3.10)
 * Django 4.0 (Python 3.8, 3.9 and 3.10)
 * Django 4.1 (Python 3.8, 3.9, 3.10 and 3.11)
 * Django 4.2 (Python 3.8, 3.9, 3.10 and 3.11)
 * Django main (Python 3.10 and 3.11)

.. |Build Status| image:: https://img.shields.io/github/workflow/status/ninemoreminutes/django-crum/test
   :target: https://github.com/ninemoreminutes/django-crum/actions?query=workflow%3Atest
.. |PyPI Version| image:: https://img.shields.io/pypi/v/django-crum.svg
   :target: https://pypi.python.org/pypi/django-crum/
.. |PyPI License| image:: https://img.shields.io/pypi/l/django-crum.svg
   :target: https://pypi.python.org/pypi/django-crum/
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/django-crum.svg
   :target: https://pypi.python.org/pypi/django-crum/
.. |Django Versions| image:: https://img.shields.io/pypi/djversions/django-crum.svg
   :target: https://pypi.org/project/django-crum/
.. |Read the Docs| image:: https://img.shields.io/readthedocs/django-crum.svg
   :target: http://django-crum.readthedocs.io/
