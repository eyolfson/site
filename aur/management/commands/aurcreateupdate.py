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

from django.core.management.base import BaseCommand, CommandError

from aur.models import Arch, Update

class Command(BaseCommand):
    args = 'package version architecture'
    help = 'Creates an AUR update for the specified package'

    def get_version(self):
        from eyl.version import get_version
        return str(get_version())

    def handle(self, *args, **options):
        if len(args) != 3:
            raise CommandError(self.args)

        try:
            arch = Arch.objects.get(name=args[2])
        except Arch.DoesNotExist:
            msg = 'Architecture "{}" does not exist'
            raise CommandError(msg.format(args[2]))

        Update.objects.create(arch=arch, package=args[0], version=args[1])
