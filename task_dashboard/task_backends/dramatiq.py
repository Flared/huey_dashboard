from typing import List, Dict
from .controller import BaseController


class DramatiqController(BaseController):
    name = "dramatiq"

    def enqueue_task(self, name: str, args: List, kwargs: Dict, options: Dict) -> str:
        return "foo"
