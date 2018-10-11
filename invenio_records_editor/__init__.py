# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# Invenio-Records-Editor
# is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module serving a generic record editor."""

from __future__ import absolute_import, print_function

from .ext import InvenioRecordsEditor
from .version import __version__

__all__ = ("__version__", "InvenioRecordsEditor")
