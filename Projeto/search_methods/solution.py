from agentsearch.problem import Problem
from search_methods.node import Node


class Solution:

    def __init__(self, problem: Problem, goal_node: Node):
        self.problem = problem
        self.goal_node = goal_node
        self.actions = []
        node = self.goal_node
        while node.parent is not None:
            self.actions.insert(0, node.state.action)
            node = node.parent

    @property
    def cost(self) -> int:
        return self.problem.compute_path_cost(self.actions)
