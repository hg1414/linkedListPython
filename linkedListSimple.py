from typing import Generator, Optional, Any

class Node:
    """
    A simple class to implement singly linked lists.
    
    """
    def __init__(
            self, value: Any = 0,
            next: Optional["Node"] = None
        ) -> None:
        self.value = value
        self.next = next

    def __iter__(self) -> Generator[Any, None, None]:
        """Enables iteration over nodes, as in for-loops or list()."""
        current = self
        while current:
            yield current.value
            current = current.next

    def __repr__(self) -> str:
        """Returns a representation of the node as a list."""
        return str(list(self))

    def append(self, value: Any) -> None:
        """Adds a value to the end of the linked list."""
        newNode = Node(value)
        current = self
        while current.next:
            current = current.next
        current.next = newNode

    def prepend(self, value: Any) -> "Node":
        """Adds a value to the beginning of the linked list.
        
        This method will return the new head, so it will be referenced
        instead of the old head.
        """
        return Node(value, self)
    
