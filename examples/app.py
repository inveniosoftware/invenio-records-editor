# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# Invenio-Records-Editor 
# is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Minimal Flask application example.

SPHINX-START

First install Invenio-Records-Editor, setup the application by running:

.. code-block:: console

   $ pip install -e .[all]
   $ cd examples
   $ ./app-setup.sh

Next, start the development server:

.. code-block:: console

   $ export FLASK_APP=app.py FLASK_DEBUG=1
   $ flask run

and open the example application in your browser:

.. code-block:: console

    $ open http://127.0.0.1:5000/

To reset the example application run:

.. code-block:: console

    $ ./app-teardown.sh

SPHINX-END
"""

from __future__ import absolute_import, print_function

from flask import Flask
from flask_menu import Menu
from invenio_accounts import InvenioAccounts
from invenio_accounts.views.settings import blueprint as accounts_bp
from invenio_assets import InvenioAssets
from invenio_i18n import InvenioI18N

from invenio_records_editor import InvenioRecordsEditor
from invenio_records_editor.views import create_editor_blueprint

app = Flask(__name__)
app.config.update(
    SECRET_KEY="CHANGE_ME",
)

Menu(app)
InvenioAccounts(app)
InvenioAssets(app)
InvenioI18N(app)
InvenioRecordsEditor(app)

editor_bp = create_editor_blueprint(app)
app.register_blueprint(accounts_bp)
app.register_blueprint(editor_bp)
