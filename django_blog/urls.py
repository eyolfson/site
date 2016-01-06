# Copyright 2014 Jon Eyolfson
#
# This file is distributed under the GPLv3 license

from django.conf.urls import patterns, include, url

from django_blog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>[a-z0-9_-]+)/$', views.post, name='post'),
]
