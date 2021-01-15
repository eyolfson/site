# Copyright 2016 Jon Eyolfson
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

from django_aur.models import Arch, Package

class Command(BaseCommand):
    args = 'package architecture'
    help = 'Sets an AUR package unavailable'

    def get_version(self):
        from eyl.version import get_version
        return str(get_version())

    def add_arguments(self, parser):
        parser.add_argument('package')
        parser.add_argument('arch')

    def handle(self, *args, **options):
        package_name = options['package']
        arch_name = options['arch']

        try:
            arch = Arch.objects.get(name=arch_name)
        except Arch.DoesNotExist:
            msg = 'Architecture "{}" does not exist'
            raise CommandError(msg.format(arch_name))

        package = Package.objects.get_or_create(name=package_name, arch=arch)[0]
        package.is_available = False
        package.save()
