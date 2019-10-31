import os
import sys
from typing import Any, Dict

from flask import Flask, render_template, current_app
from .task_backends import load_task_logs_backend
from .helpers import register_template_helpers


def index() -> str:
    return render_template("index.html")


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("task_dashboard.default_settings")

    app.add_url_rule("/", "index", index)

    from . import blueprints

    app.register_blueprint(blueprints.tasks_bp)

    task_logs_backend_fqn = app.config["TASK_LOGS_BACKEND"]
    task_logs_backend_options = app.config["TASK_LOGS_OPTIONS"]
    app.task_logs_backend = load_task_logs_backend(
        task_logs_backend_fqn, task_logs_backend_options
    )

    @app.context_processor
    def inject_helpers() -> Dict[str, Any]:
        return {"task_logs_backend": app.task_logs_backend}

    register_template_helpers(app)

    return app
