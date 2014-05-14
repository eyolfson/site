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

from django.db import models

class Arch(models.Model):
    name = models.CharField(max_length=16, blank=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'aur_arch'
        ordering = ['name']

class Package(models.Model):
    arch = models.ForeignKey(Arch, related_name='packages')
    name = models.CharField(max_length=64, blank=False, db_index=True)
    is_available = models.BooleanField(default=True, blank=False, null=False)

    def __str__(self):
        return '{} ({})'.format(self.name, self.arch)

    class Meta:
        db_table = 'aur_package'
        ordering = ['name', 'arch']
        unique_together = ('name', 'arch')

class Update(models.Model):
    package = models.ForeignKey(Package, related_name='updates')
    version = models.CharField(max_length=64, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}-{}'.format(self.package.name, self.version,
                                 self.package.arch)

    class Meta:
        db_table = 'aur_update'
        get_latest_by = 'timestamp'
        ordering = ['package', '-timestamp']
        unique_together = ('package', 'version')
