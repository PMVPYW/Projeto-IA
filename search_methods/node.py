
from typing import Generic, TypeVar

S = TypeVar("S")


class Node(Generic[S]):

    # below we use [parent: "Node"] -> search for "forward references in Python"

    def __init__(self, state: S, parent: "Node" = None, g: float = 0, f: float = 0):
        self.state = state
        self.parent = parent
        self.g = g  # cost
        self.f = f
        self.depth = 0 if parent is None else parent.depth + 1

    def is_cycle(self, state: S):
        aux_node = self
        while True:
            if state == aux_node.state:
                return True
            aux_node = aux_node.parent
            if aux_node is None:
                return False

    def __lt__(self, other):
        return self.f < other.f

    def __str__(self):
        return f'{self.f}'
