import copy

import constants
from agentsearch.problem import Problem
from warehouse.actions import *
from warehouse.cell import Cell
from warehouse.warehouse_state import WarehouseState


class WarehouseProblemSearch(Problem[WarehouseState]):

    def __init__(self, initial_state: WarehouseState, goal_position: Cell):
        super().__init__(initial_state)
        self.actions = [ActionDown(), ActionUp(), ActionRight(),
                        ActionLeft()]
        self.goal_position = goal_position

    def get_actions(self, state: WarehouseState) -> list:
        valid_actions = []
        for action in self.actions:
            if action.is_valid(state):
                valid_actions.append(action)
        return valid_actions

    def get_successor(self, state: WarehouseState, action: Action) -> WarehouseState:
        successor = copy.copy(state)
        action.execute(successor)
        return successor

    def is_goal(self, state: WarehouseState) -> bool:
        # return self.goal_position == Cell(state.line_forklift, state.column_forklift)
        if self.initial_state.matrix[self.goal_position.line][self.goal_position.column - 1] == constants.EMPTY:
            goal = -1
        else:
            goal = 1

        if self.goal_position.line == self.initial_state.line_exit and self.goal_position.column == self.initial_state.column_exit: #se goal for saida também pode entrar por cima e por baixo
            if self.goal_position.line - 1 == state.line_forklift and self.goal_position.column == state.column_forklift:
                return True
            elif self.goal_position.line + 1 == state.line_forklift and self.goal_position.column == state.column_forklift:
                return True
        return self.goal_position.line == state.line_forklift and self.goal_position.column + goal == state.column_forklift
