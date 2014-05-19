# Copyright 2014 Jon Eyolfson
#
# This file is part of Eyl Site.
#
# Eyl Site is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# Eyl Site is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Eyl Site. If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls import patterns, include, url
from eyl import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^version/$', views.version, name='version'),

    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

    url(r'^aur/', include('django_aur.urls', namespace='aur')),
    url(r'^ssh/', include('django_ssh.urls', namespace='ssh')),
)
