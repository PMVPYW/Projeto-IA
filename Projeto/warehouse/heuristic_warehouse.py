from agentsearch.heuristic import Heuristic
from warehouse.warehouse_problemforSearch import WarehouseProblemSearch
from warehouse.warehouse_state import WarehouseState


class HeuristicWarehouse(Heuristic[WarehouseProblemSearch, WarehouseState]):

    def __init__(self):
        super().__init__()

    def compute(self, state: WarehouseState) -> float:  # Manhattan distance
        # TODO --> check with teacher
        h = 0
        goal_state = self._problem.goal_position
        h += abs(state.column_forklift - goal_state.column)
        h += abs(state.line_forklift - goal_state.line)
        return h


    def __str__(self):
        #TODO --> decide wich string we want
        return "# TODO"
