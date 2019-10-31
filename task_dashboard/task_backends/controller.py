import abc
from typing import List, Dict


class BaseController(abc.ABC):
    @abc.abstractproperty
    def name(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def enqueue_task(self, name: str, args: List, kwargs: Dict, options: Dict) -> str:
        raise NotImplementedError
