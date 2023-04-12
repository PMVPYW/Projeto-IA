
from search_methods.node import Node
from utils.node_collection import NodeCollection


class NodeQueue(NodeCollection):

    def __init__(self):
        super().__init__()

    def append(self, item: Node) -> None:
        self._list.append(item)
        self._dictionary[item.state] = item

    def pop(self) -> Node:
        if self._list:
            item = self._list.pop(0)
            self._dictionary.pop(item.state)
            return item
        else:
            raise Exception('Trying to pop from empty Queue.')

    def insert_as_first(self, item: Node) -> None:
        self._list.insert(0, item)
        self._dictionary[item.state] = item
