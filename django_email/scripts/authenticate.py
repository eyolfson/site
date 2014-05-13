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

import logging
import os

import django
from django.contrib.auth import authenticate

logger = logging.getLogger('email')

try:
    with os.fdopen(3) as f:
        username, password = f.read().split('\0')[:2]
except Exception as e:
    logger.error(e)
    exit(111)

django.setup()
user = authenticate(username=username, password=password)
if user is None:
    exit(1)
