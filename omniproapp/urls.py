# -*- coding: utf-8 -*-
from django.conf.urls import url
from omniproapp.views import list

urlpatterns = [
    url(r'^list/$', list, name='list'),
    # url(r'^list/$', list, name='list'),
]