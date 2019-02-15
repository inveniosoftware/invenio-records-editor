# -*- coding: utf-8 -*-
#
# Copyright (C) 2018-2019 CERN.
#
# Invenio-Records-Editor
# is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Registered views for our record editor module."""

from __future__ import absolute_import, print_function

import copy

from flask import Blueprint, abort, current_app, render_template, request
from invenio_jsonschemas.proxies import current_jsonschemas

from .permissions import need_editor_permissions


def create_editor_blueprint(app):
    """Wrapper for our blueprint to create it on demand."""
    blueprint = Blueprint(
        "invenio_records_editor",
        __name__,
        url_prefix=app.config["RECORDS_EDITOR_URL_PREFIX"],
        template_folder="templates",
        static_folder="static",
    )

    @need_editor_permissions("editor-view")
    @blueprint.route("/<string:rec_type>/")
    @blueprint.route("/<string:rec_type>/<int:recid>")
    def index(rec_type, recid=None):
        """Render a basic view, with dummy permission editor-view."""
        json_editor_config = current_app.config["RECORDS_EDITOR_UI_CONFIG"]
        if rec_type not in json_editor_config:
            abort(404)

        ui_config = copy.deepcopy(json_editor_config[rec_type])

        ui_config["recordConfig"]["apiUrl"] = "{0}{1}".format(
            request.url_root, ui_config["recordConfig"]["apiUrl"]
        )

        ui_config["recordConfig"]["schema"] = current_jsonschemas.path_to_url(
            ui_config["recordConfig"]["schema"]
        )
        return render_template(
            app.config["RECORDS_EDITOR_TEMPLATE"],
            editor_url=app.config["RECORDS_EDITOR_URL_PREFIX"],
            module_name="Invenio-Records-Editor",
            ui_config=ui_config,
        )

    return blueprint
