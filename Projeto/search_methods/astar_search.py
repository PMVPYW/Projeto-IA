from agentsearch.state import State
from search_methods.informed_search import InformedSearch
from search_methods.node import Node


class AStarSearch(InformedSearch):

    # In this version we don't assume that the heuristic is consistent.

    # f = g + h
    def add_successor_to_frontier(self, successor: State, parent: Node) -> None:
        g = parent.g + successor.action.cost
        if successor not in self._frontier:
            if successor not in self._explored:
                f = g + self.heuristic.compute(successor)
                self._frontier.append(Node(successor, parent, g, f))
        elif g < self._frontier[successor].g:
            del self._frontier[successor]
            f = g + self.heuristic.compute(successor)
            self._frontier.append(Node(successor, parent, g, f))

    def __str__(self):
        return "A* search"
