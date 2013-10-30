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
from crum import *


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

    def get(self, request, format=None):
        if request.QUERY_PARAMS.get('raise', ''):
            raise RuntimeError()
        if request.QUERY_PARAMS.get('impersonate', ''):
            with impersonate(None):
                current_user = six.text_type(get_current_user())
        else:
            current_user = six.text_type(get_current_user())
        return Response(current_user)

api_index = ApiIndexView.as_view()
