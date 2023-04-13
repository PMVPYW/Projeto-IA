
import heapq

from utils.node_collection import NodeCollection
from search_methods.node import Node
from agentsearch.state import State

#  In this class, self.list works as a heap (see https://en.wikipedia.org/wiki/Heap_(data_structure))


class NodePriorityQueue(NodeCollection):

    def __init__(self):
        super().__init__()

    def append(self, item: Node) -> None:
        entry = (item.f, item)  # item.f is the value by which the priority queue is organized
        self._dictionary[item.state] = entry
        heapq.heappush(self._list, entry)

    def pop(self):
        if self._list:
            item = heapq.heappop(self._list)[1]
            self._dictionary.pop(item.state)
            return item
        else:
            raise Exception('Trying to pop from empty PriorityQueue.')

    def __getitem__(self, key: State):
        return self._dictionary.get(key)[1]

    def __delitem__(self, key: State):
        if not self._list:
            raise Exception('Trying to delete from empty PriorityQueue.')
        try:
            entry = self._dictionary.pop(key)
            self._list.remove(entry)
            heapq.heapify(self._list)
        except ValueError:
            raise KeyError(str(key) + ' is not in the priority queue.')

    def remove_last(self):
        if self._list:
            item = self._list.pop()[1]
            self._dictionary.pop(item.state)
            heapq.heapify(self._list)
            return item
        else:
            raise Exception('Trying to delete from empty PriorityQueue.')
