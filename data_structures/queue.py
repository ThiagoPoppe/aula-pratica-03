from typing import Any

from data_structures.exceptions import QueueEmptyError
from data_structures.exceptions import QueueLimitReachedError


class Queue:
    def __init__(self, max_size: int = None) -> None:
        self.size = 0
        self.elements = []
        self.max_size = max_size

    def insert(self, element: Any) -> None:
        if self.max_size is not None:
            if self.size == self.max_size:
                raise QueueLimitReachedError()

        self.elements.append(element)
        self.size += 1

    def remove(self) -> Any:
        if self.size == 0:
            raise QueueEmptyError()
        
        element = self.elements.pop(0)
        self.size -= 1

        return element
