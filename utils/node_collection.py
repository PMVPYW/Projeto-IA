
from abc import ABC, abstractmethod

from search_methods.node import Node
from agentsearch.state import State


class NodeCollection(ABC):

    def __init__(self):
        self._list = []
        self._dictionary = {}

    @abstractmethod
    def append(self, item: Node) -> None:
        pass

    @abstractmethod
    def pop(self) -> Node:
        pass

    def clear(self):
        self._list.clear()
        self._dictionary.clear()

    def __len__(self):
        return len(self._list)

    def __contains__(self, key: State) -> bool:
        return key in self._dictionary

    def __getitem__(self, key: State):
        return self._dictionary.get(key)

    def __delitem__(self, key: State):
        try:
            node = self._dictionary[key]
            self._list.remove(node)
            del self._dictionary[key]
        except ValueError:
            raise KeyError(str(key) + ' is not in the priority queue.')
