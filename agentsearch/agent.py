
from agentsearch.problem import Problem
from agentsearch.heuristic import Heuristic
from search_methods.astar_search import AStarSearch
from search_methods.solution import Solution


class Agent:

    def __init__(self):
        self.environment = None
        self.search_method = AStarSearch()
        self.heuristic = None
        self.solution = None

    def solve_problem(self, problem: Problem) -> Solution:
        self.environment = problem.initial_state
        if self.heuristic is not None:
            problem.heuristic = self.heuristic
            self.heuristic.problem = problem
        self.solution = self.search_method.search(problem)
        return self.solution

    def execute_solution(self) -> None:
        if self.solution:
            for action in self.solution.actions:
                action.execute(self.environment)
            print('Solution cost: ', self.solution.cost)
        else:
            print('No solution to be executed')

    def stop(self) -> None:
        self.search_method.stop()

    def has_been_stopped(self) -> bool:
        return self.search_method.stopped

    def add_heuristic(self, heuristic: Heuristic) -> None:
        self.heuristics.append(heuristic)
