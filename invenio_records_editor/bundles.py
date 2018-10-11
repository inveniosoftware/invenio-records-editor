# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# Invenio-Records-Editor
# is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.


"""Bundle definition for record editor."""

from __future__ import absolute_import, division, print_function

from flask_assets import Bundle
from invenio_assets import NpmBundle

EDITOR_PATH = "node_modules/@inveniosoftware/invenio-records-editor-js/dist"

js = NpmBundle(
    "%s/inline.bundle.js" % EDITOR_PATH,
    "%s/polyfills.bundle.js" % EDITOR_PATH,
    "%s/vendor.bundle.js" % EDITOR_PATH,
    "%s/main.bundle.js" % EDITOR_PATH,
    depends=("%s/*.js" % EDITOR_PATH),
    filters="uglifyjs",
    output="gen/invenio-records-editor-js.%(version)s.js",
    npm={"@inveniosoftware/invenio-records-editor-js": "0.0.3"},
)
"""Default Editor JavaScript bundle with Angular4."""

css = Bundle(
    "%s/styles.bundle.css" % EDITOR_PATH,
    filters="cleancssurl",
    output="gen/invenio-records-editor-js.%(version)s.css",
)
"""Default Editor CSS bundle with bootstrap, toastr"""
