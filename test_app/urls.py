# Django
from django.conf.urls import patterns, url

urlpatterns = patterns('test_app.views', *[
    url(r'^$', 'index', name='index'),
])
