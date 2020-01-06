from typing import Any, Dict, List

from .controller import BaseController


class DramatiqController(BaseController):
    name = "dramatiq"

    def enqueue_task(
        self,
        name: str,
        args: List[Any],
        kwargs: Dict[str, Any],
        options: Dict[str, Any],
    ) -> str:
        return "foo"
