from typing import Any

from data_structures.exceptions import StackEmptyError
from data_structures.exceptions import StackLimitReachedError


class Stack:
    def __init__(self, max_size: int = None) -> None:
        self.size = 0
        self.elements = []
        self.max_size = max_size

    def push(self, element: Any) -> None:
        if self.max_size is not None:
            if self.size == self.max_size:
                raise StackLimitReachedError()

        self.elements.insert(0, element)
        self.size += 1

    def pop(self) -> Any:
        if self.size == 0:
            raise StackEmptyError()

        element = self.elements.pop(0)
        self.size -= 1

        return element
