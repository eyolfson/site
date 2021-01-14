# Copyright 2014 Jon Eyolfson
#
# This file is distributed under the GPLv3 license

from django.urls import include, path

from django_blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.post, name='post'),
]
