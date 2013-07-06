.. Django-CRUM documentation master file, created by
   sphinx-quickstart on Sat Jul  6 00:44:15 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Django-CRUM
===========

**Django-CRUM (Current Request User Middleware)** captures the current request
and user in thread local storage.

It enables apps to check permissions, capture audit trails or otherwise access
the current request and user without requiring the request object to be passed
directly. It also offers a context manager to allow for temporarily
impersonating another user.

It is tested against Python 2.6 and 2.7 using Django 1.4, 1.5 and 1.6.

Installation
------------

Install the application from PYPI::

    pip install django-crum

Then, add ``CurrentRequestUserMiddleware`` to your ``MIDDLEWARE_CLASSES``
setting::

    MIDDLEWARE_CLASSES += ('crum.CurrentRequestUserMiddleware',)

*That's it!*

Usage
-----

The `crum` package exports three functions as its public API.

get_current_request()
~~~~~~~~~~~~~~~~~~~~~

``get_current_request`` returns the current request instance, or ``None`` if
called outside the scope of a request.

For example, the ``Comment`` model below overrides its ``save`` method to track
the IP address of each commenter::

    from django.db import models
    from crum import get_current_request
    
    class Comment(models.Model):
        created = models.DateTimeField(auto_now_add=True)
        comment = models.TextField()
        remote_addr = models.CharField(blank=True, default='')

        def save(self, *args, **kwargs):
            request = get_current_request()
            if request and not self.remote_addr:
                self.remote_addr = request.META['REMOTE_ADDR']
            super(Comment, self).save(*args, **kwargs)

get_current_user()
~~~~~~~~~~~~~~~~~~

``get_current_user`` returns the user associated with the current request, or
``None`` if no user is available.

If using the built-in ``User`` model from ``django.contrib.auth``, the returned
value may be the special ``AnonymousUser``, which won't have a primary key.

For example, the ``Thing`` model below records the user who created it as well
as the last user who modified it::

    from django.db import models
    from crum import get_current_user
    
    class Thing(models.Model):
        created = models.DateTimeField(auto_now_add=True)
        created_by = models.ForeignKey('auth.User', blank=True, null=True,
                                       default=None)
        modified = models.DateTimeField(auto_now=True)
        modified_by = models.ForeignKey('auth.User', blank=True, null=True,
                                        default=None)

        def save(self, *args, **kwargs):
            user = get_current_user()
            if user and not user.pk:
                user = None
            if not self.pk:
                self.created_by = user
            self.modified_by = user
            super(Thing, self).save(*args, **kwargs)

impersonate(user=None)
~~~~~~~~~~~~~~~~~~~~~~

``impersonate`` is a context manager used to temporarily change the current
user as returned by ``get_current_user``.  It is typically used to perform an
action on behalf of a user or disable the default behavior of
``get_current_user``.

For example, a background task may need to create or update ``Things`` objects
when there is no active request or user (such as from a management command)::

    from crum import impersonate

    def create_thing_for_user(user):
        with impersonate(user):
            # This Thing will indicated it was created by the given user.
            user_thing = Thing.objects.create()
        # But this Thing won't have a created_by user.
        other_thing = Thing.objects.create()

When running from within a view, ``impersonate`` may be used to prevent certain
actions from being attributed to the requesting user::

    from django.template.response import TemplateResponse
    from crum import impersonate
    
    def get_my_things(request):
        # Whenever this view is accessed, trigger some cleanup of Things.
        with impersonate(None):
            Thing.objects.cleanup()
        my_things = Thing.objects.filter(created_by=request.user)
        return TemplateResponse(request, 'my_things.html',
                                {'things': my_things})
