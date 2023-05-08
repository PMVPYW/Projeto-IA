from agentsearch.heuristic import Heuristic
from warehouse.warehouse_problemforSearch import WarehouseProblemSearch
from warehouse.warehouse_state import WarehouseState
from math import sqrt


class HeuristicWarehouse(Heuristic[WarehouseProblemSearch, WarehouseState]):

    def __init__(self):
        super().__init__()

    def compute(self, state: WarehouseState) -> float:  # Manhattan distance para obter catetos e calcular hipotenusa
        print("compute: ", end="")
        goal_state = self._problem.goal_position
        cateto1 = abs(state.column_forklift - goal_state.column) ** 2
        cateto2 = abs(state.line_forklift - goal_state.line) ** 2
        print(sqrt(cateto1 + cateto2))
        return sqrt(cateto1 + cateto2)

    def __str__(self):
        # TODO --> decide wich string we want
        return "# TODO"
