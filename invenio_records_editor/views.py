# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# Invenio-Records-Editor
# is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Registered views for our record editor module."""

from __future__ import absolute_import, print_function

from flask import Blueprint, current_app, render_template, request
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

    @blueprint.route("/<string:rec_type>")
    @blueprint.route("/<string:rec_type>/<int:recid>")
    @need_editor_permissions("editor-view")
    def edit_record(rec_type, recid=None):
        """Render a basic view, with dummy permission editor-view."""
        ui_config = {}
        json_editor_config = current_app.config["RECORDS_EDITOR_UI_CONFIG"]
        endpoint_config = json_editor_config.get(rec_type)
        ui_config.update(endpoint_config)

        api_url = "{0}{1}".format(
            request.url_root, endpoint_config["recordConfig"]["apiUrl"]
        )
        if recid:
            api_url = "{0}{1}".format(api_url, recid)

        ui_config["recordConfig"]["apiUrl"] = api_url
        ui_config["recordConfig"][
            "$schema"
        ] = current_jsonschemas.path_to_url(
            endpoint_config["recordConfig"]["$schema"]
        )
        import ipdb

        ipdb.set_trace()
        return render_template(
            app.config["RECORDS_EDITOR_TEMPLATE"],
            editor_url=app.config["RECORDS_EDITOR_URL_PREFIX"],
            module_name="Invenio-Records-Editor",
            ui_config=ui_config,
        )

    return blueprint

    @need_editor_permissions("editor-view")
    def create_record(rec_type):
        """Render a basic view, with dummy permission editor-view."""
        ui_config = {}
        json_editor_config = current_app.config["RECORDS_EDITOR_UI_CONFIG"]
        endpoint_config = json_editor_config.get(rec_type)
        ui_config.update(endpoint_config)

        ui_config["record_config"]["apiUrl"] = "{0}{1}{2}".format(
            request.url_root, endpoint_config["record_config"]["apiUrl"], recid
        )
        ui_config["record_config"][
            "$schema"
        ] = current_jsonschemas.path_to_url(
            endpoint_config["record_config"]["$schema"]
        )

        return render_template(
            app.config["RECORDS_EDITOR_TEMPLATE"],
            editor_url=app.config["RECORDS_EDITOR_URL_PREFIX"],
            module_name="Invenio-Records-Editor",
            ui_config=ui_config,
        )

    return blueprint
