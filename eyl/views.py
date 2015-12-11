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

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from django_aur.models import Update
from django_blog.models import Post

def home(request):
    try:
        blog_post = Post.objects.latest()
    except:
        blog_post = None
    context = {
        'aur_updates': Update.objects.filter(package__is_available=True
            ).order_by('-timestamp')[:5],
        'blog_post': blog_post,
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def research(request):
    return render(request, 'research.html')

def version(request):
    import django
    import sys
    import eyl.version
    import django_ssh.version
    import django_gitolite.version
    context = {'python_version': '{}.{}.{}'.format(*sys.version_info[:3]),
               'django_version': django.get_version(),
               'site_version': eyl.version.get_version(),
               'django_ssh_version': django_ssh.version.get_version(),
               'django_gitolite_version': django_gitolite.version.get_version()}
    return render(request, 'version.html', context)
