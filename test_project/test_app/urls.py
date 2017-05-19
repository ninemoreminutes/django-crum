# Django
from django.conf.urls import url

# Test App
from test_project.test_app.views import index, api_index


app_name = 'test_app'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^api/$', api_index, name='api_index'),
]
