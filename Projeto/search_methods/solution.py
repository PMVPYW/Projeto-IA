from agentsearch.problem import Problem
from search_methods.node import Node
from warehouse.cell import Cell


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

    def get_path(self):
        path = []
        for a in self.actions:
            print(a)
            s = self.problem.get_successor(self.problem.initial_state, a)
            path.append(Cell(s.line_forklift, s.column_forklift))
        return path

    def __str__(self):
        str = ""
        for x in self.actions:
            str+=f" {x} "
        return str
