# Python
from __future__ import with_statement
from __future__ import unicode_literals
import imp
import json

# Django
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils import six

# Django-CRUM
from crum import *


class TestCRUM(TestCase):
    """Test cases for the CRUM app."""

    def setUp(self):
        super(TestCRUM, self).setUp()
        self.user_password = User.objects.make_random_password()
        self.user = User.objects.create_user('user', 'user@example.com',
                                             self.user_password)

    def test_middleware(self):
        # For test coverage.
        import crum
        imp.reload(crum)
        # Test anonymous user.
        self.assertEqual(get_current_user(), None)
        url = reverse('test_app:index')
        response = self.client.get(url)
        response_content = response.content.decode('utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content, 'AnonymousUser')
        self.assertEqual(get_current_user(), None)
        # Test logged in user.
        self.client.login(username=self.user.username,
                          password=self.user_password)
        response = self.client.get(url)
        response_content = response.content.decode('utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content, six.text_type(self.user))
        self.assertEqual(get_current_user(), None)
        # Test impersonate context manager.
        with impersonate(self.user):
            self.assertEqual(get_current_user(), self.user)
        self.assertEqual(get_current_user(), None)
        # Test impersonate(None) within view requested by logged in user.
        self.client.login(username=self.user.username,
                          password=self.user_password)
        response = self.client.get(url + '?impersonate=1')
        response_content = response.content.decode('utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content, six.text_type(None))
        self.assertEqual(get_current_user(), None)
        # Test when request raises exception.
        try:
            response = self.client.get(url + '?raise=1')
        except RuntimeError:
            response = None
        self.assertEqual(response, None)
        self.assertEqual(get_current_user(), None)

    def test_middleware_with_rest_framework(self):
        # Test anonymous user.
        self.assertEqual(get_current_user(), None)
        url = reverse('test_app:api_index')
        response = self.client.get(url)
        response_content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content, six.text_type('AnonymousUser'))
        self.assertEqual(get_current_user(), None)
        # Test logged in user.
        self.client.login(username=self.user.username,
                          password=self.user_password)
        response = self.client.get(url)
        response_content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content, six.text_type(self.user))
        self.assertEqual(get_current_user(), None)
        # Test impersonate(None) within view requested by logged in user.
        self.client.login(username=self.user.username,
                          password=self.user_password)
        response = self.client.get(url + '?impersonate=1')
        response_content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content, six.text_type(None))
        self.assertEqual(get_current_user(), None)
        # Test when request raises exception.
        try:
            response = self.client.get(url + '?raise=1')
        except RuntimeError:
            response = None
        self.assertEqual(response, None)
        self.assertEqual(get_current_user(), None)
