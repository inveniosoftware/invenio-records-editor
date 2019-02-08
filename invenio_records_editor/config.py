# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
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
"""Editor ui config."""

"""
RECORDS_EDITOR_UI_CONFIG = {
    "items": {
        "recordConfig": {
            "apiUrl": "api/items/",
            "$schema": "items/item-v1.0.0.json",
        },
        "editorConfig": {
            "schemaOptions": {
                "alwaysShow": [
                    "legacy_id",
                    "shelf",
                    "description",
                    "circulation_restriction",
                    "medium",
                    "legacy_library_id",
                ],
                "properties": {
                    "$schema": {"hidden": True},
                    "document": {"hidden": True},
                    "internal_location": {"hidden": True},
                    "circulation_status": {"hidden": True},
                },
            },
        },
    },
    "documents": {
        "recordConfig": {
            "apiUrl": "api/documents/",
            "$schema": "documents/document-v1.0.0.json",
        },
        "editorConfig": {
            "schemaOptions": {
                "alwaysShow": ["title", "abstracts", "authors"],
                "properties": {
                    "$schema": {"hidden": True},
                    "circulation": {"hidden": True},
                },
            },
        },
    },
    "locations": {
        "record_editor": {
            "apiUrl": "api/locations/",
            "$schema": "locations/location-v1.0.0.json",
        },
        "editorConfig": {
            "schemaOptions": {
                "alwaysShow": [
                    "location_pid",
                    "name",
                    "address",
                    "email",
                    "phone",
                    "notes",
                ],
                "properties": {"$schema": {"hidden": True}},
            },
        },
    },
    "internal-locations": {
        "recordConfig": {
            "apiUrl": "api/internal-locations/",
            "$schema": "internal_locations/internal_location-v1.0.0.json",
        },
        "editorConfig": {
            "schemaOptions": {
                "alwaysShow": [
                    "legacy_id",
                    "location_pid",
                    "name",
                    "physical_location",
                    "notes",
                ],
                "properties": {
                    "$schema": {"hidden": True},
                    "location": {"hidden": True},
                },
            },
        },
    },
}
"""