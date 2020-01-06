from task_logs import WriterBackend


def setup_fakedata(backend: WriterBackend):
    backend.write_enqueued(
        task_id="task-1",
        task_name="task1",
        task={
            "queue": "default",
            "task_path": "tests.task1",
            "execute_at": None,
            "args": [1],
            "kwargs": {"a": "b"},
            "options": {},
        },
    )

    backend.write_dequeued(task_id="task-1", task_name="task1")
    backend.write_completed(task_id="task-1", task_name="task1", result=None)
