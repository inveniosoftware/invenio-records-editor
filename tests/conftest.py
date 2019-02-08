# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# Invenio-Records-Editor
# is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Pytest configuration."""

from __future__ import absolute_import, print_function

import shutil
import tempfile

import pytest
from flask import Flask
from invenio_accounts import InvenioAccounts
from invenio_assets import InvenioAssets

from invenio_records_editor import InvenioRecordsEditor


@pytest.fixture()
def editor_config():
    """Editor example config."""
    return RECORDS_EDITOR_UI_CONFIG = {
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


@pytest.fixture()
def instance_path():
    """Temporary instance path."""
    path = tempfile.mkdtemp()
    yield path
    shutil.rmtree(path)


@pytest.fixture()
def base_app(instance_path, editor_config):
    """Flask application fixture."""
    app_ = Flask("testapp", instance_path=instance_path)

    app_.config.update(
        SECRET_KEY="SECRET_KEY",
        TESTING=True
    )
    app_.config.update(editor_config)

    InvenioAccounts(app_)
    InvenioAssets(app_)
    InvenioRecordsEditor(app_)
    return app_


@pytest.fixture()
def app(base_app):
    """Flask application fixture."""
    with base_app.app_context():
        yield base_app
