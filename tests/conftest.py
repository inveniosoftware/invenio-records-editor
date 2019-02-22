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
from flask_menu import Menu
from invenio_accounts import InvenioAccounts
from invenio_assets import InvenioAssets
from invenio_jsonschemas import InvenioJSONSchemas

from invenio_records_editor.ext import InvenioRecordsEditor
from invenio_records_editor.views import create_editor_blueprint


@pytest.fixture()
def editor_config():
    """Editor example config."""
    config = {
        "items": {
            "recordConfig": {
                "apiUrl": "api/items/",
                "schema": "items/item-v1.0.0.json",
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
                }
            },
        }
    }
    return config


@pytest.fixture()
def instance_path():
    """Temporary instance path."""
    path = tempfile.mkdtemp()
    yield path
    shutil.rmtree(path)


@pytest.fixture()
def base_app(instance_path, editor_config):
    """Flask application fixture."""
    app = Flask("testapp", instance_path=instance_path)

    app.config.update(
        SECRET_KEY="SECRET_KEY", TESTING=True, SERVER_NAME="localhost"
    )
    app.config.update(RECORDS_EDITOR_UI_CONFIG=editor_config)

    InvenioAccounts(app)
    InvenioAssets(app)
    InvenioJSONSchemas(app)
    InvenioRecordsEditor(app)
    Menu(app)

    from invenio_accounts.views.settings import blueprint
    app.register_blueprint(blueprint)

    app.register_blueprint(create_editor_blueprint(app))
    return app


@pytest.fixture()
def app(base_app):
    """Flask application fixture."""
    with base_app.app_context():
        yield base_app
