# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# Invenio-Record-Editor is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Registered views for our record editor module."""

from __future__ import absolute_import, print_function

from flask import Blueprint, render_template

from .permissions import need_editor_permissions


def create_editor_blueprint(app):
    """Wrapper for our blueprint to create it on demand."""
    blueprint = Blueprint(
        "invenio_record_editor",
        __name__,
        url_prefix=app.config["RECORD_EDITOR_URL_PREFIX"],
        template_folder="templates",
        static_folder="static",
    )

    @blueprint.route("/")
    @need_editor_permissions("editor-view")
    def index():
        """Render a basic view, with dummy permission editor-view."""
        return render_template(
            "invenio_record_editor/base.html",
            editor_url=app.config["RECORD_EDITOR_URL_PREFIX"],
            module_name="Invenio-Record-Editor",
        )

    return blueprint
