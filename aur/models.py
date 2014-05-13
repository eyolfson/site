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

class Update(models.Model):
    arch = models.ForeignKey(Arch)
    package = models.CharField(max_length=64, blank=False, db_index=True)
    version = models.CharField(max_length=64, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}-{}'.format(self.package, self.version, self.arch)

    class Meta:
        unique_together = ('arch', 'package', 'version')
