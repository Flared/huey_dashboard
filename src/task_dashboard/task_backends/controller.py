import abc
from typing import Any, Dict, List


class BaseController(abc.ABC):
    @abc.abstractproperty
    def name(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def enqueue_task(
        self,
        name: str,
        args: List[Any],
        kwargs: Dict[str, Any],
        options: Dict[str, Any],
    ) -> str:
        raise NotImplementedError
