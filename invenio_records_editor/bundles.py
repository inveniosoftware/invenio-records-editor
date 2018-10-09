# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# Invenio-Records-Editor
# is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.


"""Bundle definition for record editor."""

from __future__ import absolute_import, division, print_function

from invenio_assets import NpmBundle

js = NpmBundle(
    "node_modules/invenio-records-editor-js/dist/inline.bundle.js",
    "node_modules/invenio-records-editor-js/dist/polyfills.bundle.js",
    "node_modules/invenio-records-editor-js/dist/vendor.bundle.js",
    "node_modules/invenio-records-editor-js/dist/main.bundle.js",
    depends=("node_modules/invenio-records-editor-js/dist/*.js"),
    filters="uglifyjs",
    output="gen/invenio-records-editor-js.%(version)s.js",
    npm={"invenio-records-editor-js": "0.0.1"},
)
"""Default Editor JavaScript bundle with Angular4."""

css = NpmBundle(
    "node_modules/invenio-records-editor-js/dist/styles.bundle.css",
    filters="cleancssurl",
    output="gen/invenio-records-editor-js.%(version)s.css",
)
"""Default Editor CSS bundle with bootstrap, font-awesome, kate, toastr"""
