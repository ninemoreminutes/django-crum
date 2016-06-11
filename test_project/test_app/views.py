# Python
from __future__ import with_statement
from __future__ import unicode_literals

# Django
from django.http import HttpResponse
from django.views.generic.base import View
from django.utils import six

# Django-REST-Framework
from rest_framework.response import Response
from rest_framework.views import APIView

# Django-CRUM
from crum import get_current_user, impersonate


class IndexView(View):

    def get(self, request):
        if request.GET.get('raise', ''):
            raise RuntimeError()
        if request.GET.get('impersonate', ''):
            with impersonate(None):
                current_user = six.text_type(get_current_user())
        else:
            current_user = six.text_type(get_current_user())
        return HttpResponse(current_user, content_type='text/plain')

index = IndexView.as_view()


class ApiIndexView(APIView):

    def initialize_request(self, request, *args, **kwargs):
        """Store the REST Framework request on the Django request."""
        req = super(ApiIndexView, self).initialize_request(request, *args,
                                                           **kwargs)
        request.drf_request = req
        return req

    def get(self, request, format=None):
        if request.query_params.get('raise', ''):
            raise RuntimeError()
        if request.query_params.get('impersonate', ''):
            with impersonate(None):
                current_user = six.text_type(get_current_user())
        else:
            current_user = six.text_type(get_current_user())
        return Response(current_user)

api_index = ApiIndexView.as_view()
