from typing import Optional

from flask import Blueprint, abort, current_app, render_template
from task_logs.backends.backend import EnqueuedLog

bp = Blueprint("tasks", __name__, url_prefix="/tasks")


@bp.route("/")
def list() -> str:
    logs = current_app.task_logs_backend.all()
    return render_template("tasks/list.html", logs=logs)


@bp.route("/<string:task_id>/")
def show(task_id: str) -> str:
    logs = current_app.task_logs_backend.find_task(task_id)
    enqueued_log: Optional[EnqueuedLog] = None
    if not logs:
        abort(404)

    last_log = logs[0]
    if logs[-1]["type"] == "enqueued":
        enqueued_log = logs[-1]

    return render_template(
        "tasks/show.html", logs=logs, enqueued_log=enqueued_log, last_log=last_log
    )
