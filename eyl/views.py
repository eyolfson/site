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

from aur.models import Update
from django_ssh.forms import KeyForm
from django_ssh.models import Key

def home(request):
    context = {'aur_updates': Update.objects.order_by('-timestamp')[:5]}
    return render(request, 'home.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        key_form = KeyForm(request.user, request.POST, request.FILES)
        if key_form.is_valid():
            key_form.create()
            return redirect('profile')
    else:
        key_form = KeyForm(request.user)
    keys = Key.objects.filter(user=request.user)
    return render(request, 'profile.html', {'keys': keys, 'key_form': key_form})

@login_required
def profile_remove(request, key_id):
    try:
        key = Key.objects.get(pk=key_id, user=request.user)
        key.delete()
    except Key.DoesNotExist:
        pass
    return redirect('profile')
