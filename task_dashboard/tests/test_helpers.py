from task_dashboard.helpers import repr_task, titlize


def test_titlize():
    assert titlize("task 1") == "Task 1"
    assert titlize("another task") == "Another Task"


def test_repr_task():
    assert (
        repr_task(
            {
                "task_id": "task-1",
                "task_name": "task1",
                "task": {
                    "task_path": "tests.task1",
                    "args": [1],
                    "kwargs": {"a": "b"},
                },
            }
        )
        == "tests.task1(1, a='b')"
    )

    assert repr_task({"task_id": "task-1", "task_name": "task1"}) == "task1"

    assert repr_task(None) == "Task data missing!"
