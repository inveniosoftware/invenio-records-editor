# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# Invenio-Records-Editor
# is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Module tests."""

from __future__ import absolute_import, print_function

from flask import Flask, render_template_string, url_for

from invenio_records_editor.ext import InvenioRecordsEditor


def test_version():
    """Test version import."""
    from invenio_records_editor import __version__

    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask("testapp")
    ext = InvenioRecordsEditor(app)
    assert "invenio-records-editor" in app.extensions

    app = Flask("testapp")
    ext = InvenioRecordsEditor()
    assert "invenio-records-editor" not in app.extensions
    ext.init_app(app)
    assert "invenio-records-editor" in app.extensions


def test_view(app):
    """Test views."""
    with app.test_client() as client:
        resp = client.get(url_for('invenio_records_editor.index',
                          rec_type="items"))
        assert resp.status_code == 200

        resp = client.get(url_for('invenio_records_editor.index',
                          rec_type="items", recid=20))
        assert resp.status_code == 200
