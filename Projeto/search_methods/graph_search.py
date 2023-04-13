
from abc import abstractmethod
from typing import Generic, TypeVar, Type

from agentsearch.problem import Problem
from agentsearch.state import State
from utils.node_collection import NodeCollection
from search_methods.search_method import SearchMethod
from search_methods.solution import Solution
from search_methods.node import Node

T = TypeVar("T", bound=NodeCollection)


class GraphSearch(SearchMethod, Generic[T]):

    def __init__(self, collection_type: Type[T]):
        super().__init__()
        self._frontier = collection_type()
        self._explored = set()

    def search(self, problem: Problem) -> Solution:
        self.reset()
        self.stopped = False
        return self.graph_search(problem)

    # function GRAPH_SEARCH(problem) returns a solution, or failure
    #   initialize the frontier using the initial state of problem
    #   initialize the explored set to be empty
    #   while( frontier is not empty)
    #       remove the first node from the frontier
    #       if the node contains a goal state then return the corresponding solution
    #            add the node to the explored set
    #           expand the node, adding the resulting nodes to the frontier only if not in the frontier or explored set
    #   return failure

    def graph_search(self, problem: Problem) -> Solution:
        self._frontier.clear()
        self._explored.clear()
        self._frontier.append(Node(problem.initial_state))

        while len(self._frontier) != 0 and not self.stopped:
            node = self._frontier.pop()
            state = node.state
            if problem.is_goal(state):
                return Solution(problem, node)
            self._explored.add(state)
            actions = problem.get_actions(state)
            for action in actions:
                successor = problem.get_successor(state, action)
                self.add_successor_to_frontier(successor, node)
            self.compute_statistics(len(actions))

    @abstractmethod
    def add_successor_to_frontier(self, successor: State, parent: Node) -> None:
        pass

    def compute_statistics(self, successors_size: int) -> None:
        self.num_expanded_nodes += 1
        self.num_generated_states += successors_size
        self.max_frontier_size = max(self.max_frontier_size, len(self._frontier))
