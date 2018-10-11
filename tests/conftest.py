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


@pytest.yield_fixture()
def instance_path():
    """Temporary instance path."""
    path = tempfile.mkdtemp()
    yield path
    shutil.rmtree(path)


@pytest.fixture()
def base_app(instance_path):
    """Flask application fixture."""
    app_ = Flask("testapp", instance_path=instance_path)
    app_.config.update(SECRET_KEY="SECRET_KEY", TESTING=True)
    InvenioAccounts(app_)
    InvenioAssets(app_)
    InvenioRecordsEditor(app_)
    return app_


@pytest.yield_fixture()
def app(base_app):
    """Flask application fixture."""
    with base_app.app_context():
        yield base_app
