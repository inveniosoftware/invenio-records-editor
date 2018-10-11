# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# Invenio-Records-Editor
# is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Invenio record editor module extension."""

from __future__ import absolute_import, print_function

from . import config


class InvenioRecordsEditor(object):
    """Invenio-Records-Editor extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        app.extensions["invenio-records-editor"] = self

    def init_config(self, app):
        """Initialize configuration."""
        # Use theme's base template if theme is installed
        if "BASE_TEMPLATE" in app.config:
            app.config.setdefault(
                "RECORDS_EDITOR_BASE_TEMPLATE", app.config["BASE_TEMPLATE"]
            )
        for k in dir(config):
            if k.startswith("RECORDS_EDITOR_"):
                app.config.setdefault(k, getattr(config, k))
