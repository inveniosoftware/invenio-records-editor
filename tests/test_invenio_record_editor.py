# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# Invenio-Record-Editor is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Module tests."""

from __future__ import absolute_import, print_function

from flask import Flask

from invenio_record_editor import InvenioRecordEditor


def test_version():
    """Test version import."""
    from invenio_record_editor import __version__
    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask('testapp')
    ext = InvenioRecordEditor(app)
    assert 'invenio-record-editor' in app.extensions

    app = Flask('testapp')
    ext = InvenioRecordEditor()
    assert 'invenio-record-editor' not in app.extensions
    ext.init_app(app)
    assert 'invenio-record-editor' in app.extensions


def test_view(app):
    """Test view."""
    InvenioRecordEditor(app)
    with app.test_client() as client:
        res = client.get("/")
        assert res.status_code == 200
        assert 'Welcome to Invenio-Record-Editor' in str(res.data)
