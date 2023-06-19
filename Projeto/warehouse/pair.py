import copy

from warehouse.cell import Cell


class Pair:
    def __init__(self, cell1, cell2):
        self.cell1 = cell1
        self.cell2 = cell2
        self.cost = 0
        self.path = []

    def get_path(self, solution):
        if solution is None:
            return None
        problem = copy.deepcopy(solution.problem)
        problem.initial_state.line_forklift = self.cell1.line
        problem.initial_state.column_forklift = self.cell1.column
        path = []
        for action in solution.actions:
            problem.initial_state = problem.get_successor(problem.initial_state, action)
            path.append(Cell(problem.initial_state.line_forklift, problem.initial_state.column_forklift))
        self.path = path

        return path

    def hash(self):
        return str(self.cell1.line) + "_" + str(self.cell1.column) + "_" + str(
            self.cell2.line) + "_" + str(self.cell2.column)

    def __str__(self):
        st = ""
        if len(self.path) > 0:
            p = self.path
            st = "path: ["
            for x in p:
                st += str(x) + ","
            st += "]"
        return str(self.cell1.line) + "-" + str(self.cell1.column) + " / " + str(self.cell2.line) + "-" + str(self.cell2.column) + ": " + str(self.cost) + " " + st + "\n"

