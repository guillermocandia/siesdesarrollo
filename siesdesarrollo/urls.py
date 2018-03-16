# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib import admin
from django.contrib import admin
from django.conf.urls import include


from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='API')
admin.site.site_header = 'Administración'

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^index.html$', schema_view),
    url(r'^auth/', obtain_auth_token),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
    url(r'^', include('app.tickets.urls',
        namespace='tickets'))
]
