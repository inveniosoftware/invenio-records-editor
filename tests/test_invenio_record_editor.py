# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# Invenio-Records-Editor
# is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Module tests."""

from __future__ import absolute_import, print_function

from flask import Flask, render_template_string
from invenio_accounts.views.settings import blueprint as accounts_bp

from invenio_records_editor import InvenioRecordsEditor
from invenio_records_editor.views import create_editor_blueprint


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


def _check_template():
    """Check template."""
    extended = """
        {% extends 'invenio_records_editor/editor.html' %}
        {% block header %}{% endblock %}
        {% block page_body %}{{ super() }}{% endblock %}
        {% block javascript %}{% endblock %}
    """
    rendered = render_template_string(extended)
    assert "app-root" in rendered


def test_view(app):
    """Test view."""
    editor_bp = create_editor_blueprint(app)
    app.register_blueprint(editor_bp)
    app.register_blueprint(accounts_bp)
    with app.test_request_context():
        _check_template()
