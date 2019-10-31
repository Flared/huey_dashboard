import inspect
from typing import Any, cast
from task_logs.backends.backend import ReaderBackend
from pydoc import locate


def load_task_logs_backend(class_fqn: str, options: Any) -> ReaderBackend:
    backend_cls: Any = locate(class_fqn)

    if isinstance(backend_cls, ReaderBackend):
        return backend_cls

    if not issubclass(backend_cls, ReaderBackend):
        raise ValueError(f"{backend_cls} is not a ReaderBackend class")

    return backend_cls(**options)
