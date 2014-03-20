# Copyright 2014 Jon Eyolfson
#
# This file is part of Eyl Site.
#
# Eyl Site is free software: you can redistribute it and/or modify$
# terms of the GNU General Public License as published by the Free$
# Foundation, either version 3 of the License, or (at your option)$
# version.
#
# Eyl Site is distributed in the hope that it will be useful, but $
# WARRANTY; without even the implied warranty of MERCHANTABILITY o$
# A PARTICULAR PURPOSE. See the GNU General Public License for mor$
#
# You should have received a copy of the GNU General Public Licens$
# Eyl Site. If not, see <http://www.gnu.org/licenses/>.

import logging
import os

from django.contrib.auth import authenticate

logger = logging.getLogger('email')

try:
    with os.fdopen(3) as f:
        username, password = f.read().split('\0')[:2]
except Exception as e:
    logger.error(e)
    exit(111)

user = authenticate(username=username, password=password)
if user is None:
    exit(1)
