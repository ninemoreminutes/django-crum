# Django
try:
    from django.urls import re_path
except ImportError:
    from django.conf.urls import url as re_path

# Test App
from test_project.test_app.views import index, api_index


app_name = 'test_app'

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^api/$', api_index, name='api_index'),
]
