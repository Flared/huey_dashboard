import os
import sys
from typing import Any, Dict, Optional

import werkzeug.wrappers
from flask import Flask, current_app, redirect, render_template, url_for

from .helpers import register_template_helpers
from .task_backends import load_task_logs_backend


def index() -> werkzeug.wrappers.Response:
    return redirect(url_for("tasks.list"))


def create_app(config: Optional[Dict[str, Any]] = None) -> Flask:
    app = Flask(__name__)
    app.config.from_object("task_dashboard.default_settings")
    if config:
        app.config.update(config)

    app.add_url_rule("/", "index", index)

    from . import blueprints

    app.register_blueprint(blueprints.tasks_bp)

    task_logs_backend_fqn = app.config["TASK_LOGS_BACKEND"]
    task_logs_backend_options = app.config.get("TASK_LOGS_OPTIONS", {})
    app.task_logs_backend = load_task_logs_backend(
        task_logs_backend_fqn, task_logs_backend_options
    )

    @app.context_processor
    def inject_helpers() -> Dict[str, Any]:
        return {"task_logs_backend": app.task_logs_backend}

    register_template_helpers(app)

    if app.config["TASK_LOGS_FAKEDATA"]:
        from .tests.fakedata import setup_fakedata

        setup_fakedata(app.task_logs_backend)

    return app
