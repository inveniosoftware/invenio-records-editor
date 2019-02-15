# -*- coding: utf-8 -*-
#
# Copyright (C) 2018-2019 CERN.
#
# Invenio-Records-Editor
# is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Configuration for the invenio-records-editor module."""

from .permissions import allow_all

RECORDS_EDITOR_URL_PREFIX = "/"
"""Default URL we want to serve our editor application, i.e /editor."""

RECORDS_EDITOR_VIEW_PERMISSION = allow_all
"""Default permission to access the editor."""

RECORDS_EDITOR_TEMPLATE = "invenio_records_editor/editor.html"
"""Default editor template."""

RECORDS_EDITOR_UI_CONFIG = {}
"""Editor ui config.

Example configuration could be:

.. code-block:: python

    {
        "records": {
            "recordConfig": {
                "apiUrl": "api/records/",
                "$schema": "records/record-v1.0.0.json"
            },
            "editorConfig": {
                "schemaOptions": {
                    "alwaysShow": [
                        "title",
                        "description"
                    ],
                    "properties": {
                        "$schema": {
                            "hidden": True
                        }
                    }
                }
            }
        }
    }

"""
