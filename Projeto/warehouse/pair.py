import copy

from warehouse.cell import Cell


class Pair:
    def __init__(self, cell1, cell2):
        self.cell1 = cell1
        self.cell2 = cell2
        self.cost = 0
        self.solution = None
        # TODO? --> guardar caminho e custo, verificar se coordenada é agente ou pick (picks guardados no agente(pick == agente))

    def get_path(self):
        if self.solution is None:
            return None
        problem = copy.deepcopy(self.solution.problem)
        path = []
        for action in self.solution.actions:
            problem.initial_state = problem.get_successor(problem.initial_state, action)
            path.append(Cell(problem.initial_state.line_forklift, problem.initial_state.column_forklift))
        return path

    def hash(self):
        return str(self.cell1.line) + "_" + str(self.cell1.column) + "_" + str(
            self.cell2.line) + "_" + str(self.cell2.column)

    def __str__(self):
        st = ""
        if not self.solution is None:
            p = self.get_path()
            st = "path: ["
            for x in p:
                st += str(x) + ","
            st += "]"
        return str(self.cell1.line) + "-" + str(self.cell1.column) + " / " + str(self.cell2.line) + "-" + str(self.cell2.column) + ": " + str(self.cost) + " " + st + "\n"

