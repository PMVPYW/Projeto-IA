import copy

from agentsearch.problem import Problem
from warehouse.actions import *
from warehouse.cell import Cell
from warehouse.warehouse_state import WarehouseState


class WarehouseProblemSearch(Problem[WarehouseState]):

    def __init__(self, initial_state: WarehouseState, goal_position: Cell):
        super().__init__(initial_state)
        self.actions = [ActionDown(), ActionUp(), ActionRight(),
                        ActionLeft()]  # TODO --> Ask where are this actions and why warehouse.actions is always up
        self.goal_position = goal_position

    def get_actions(self, state: WarehouseState) -> list:
        valid_actions = []
        for action in self.actions:
            if action.is_valid(state):
                valid_actions.append(action)
        return valid_actions

    def get_successor(self, state: WarehouseState, action: Action) -> WarehouseState:
        successor = copy.deepcopy(state)
        action.execute(successor)
        return successor

    def is_goal(self, state: WarehouseState) -> bool:
        # TODO //possible not wrong
        # return self.goal_position == Cell(state.line_forklift, state.column_forklift)
        fork_pos = Cell(state.line_forklift, state.column_forklift)
        fork_target1 = Cell(self.goal_position.line, self.goal_position.column - 1)
        fork_target2 = Cell(self.goal_position.line, self.goal_position.column + 1)
        return self.goal_position == fork_target1 or self.goal_position == fork_target2
