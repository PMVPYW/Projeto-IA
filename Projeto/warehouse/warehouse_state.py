import copy

import numpy as np
from PIL.ImageEnhance import Color
from numpy import ndarray

import constants
from agentsearch.state import State
from agentsearch.action import Action


class WarehouseState(State[Action]):  # podemos adicionar/alterar métodos

    def __init__(self, matrix: ndarray, rows, columns):
        super().__init__()
        # TODO //ver puzzle8
        # //question --> agent can be in exit cell?

        self.rows = rows
        self.columns = columns
        self.matrix = copy.deepcopy(matrix)  # np.full([self.rows, self.columns], fill_value=0, dtype=int)

        # possivel otimizar(dá pontos)

        for i in range(self.rows):
            if constants.FORKLIFT in self.matrix[i] or constants.EXIT in self.matrix[i]:
                for j in range(self.columns):
                    # self.matrix[i][j] = matrix[i][j] //removed
                    if self.matrix[i][j] == constants.FORKLIFT:
                        self.line_forklift = i
                        self.column_forklift = j

    def can_move_up(self) -> bool:
        if self.line_forklift == 0 or self.matrix[self.line_forklift - 1][self.column_forklift] != constants.EMPTY:
            return False
        return True

    def can_move_right(self) -> bool:
        if self.column_forklift == self.columns - 1 or self.matrix[self.line_forklift][
            self.column_forklift + 1] != constants.EMPTY:
            return False
        return True

    def can_move_down(self) -> bool:
        if self.line_forklift == self.rows - 1 or self.matrix[self.line_forklift + 1][
            self.column_forklift] != constants.EMPTY:
            return False
        return True

    def can_move_left(self) -> bool:
        if self.column_forklift == 0 or self.matrix[self.line_forklift][self.column_forklift - 1] != constants.EMPTY:
            return False
        return True

    def move_up(self) -> None:
        if not self.can_move_up():
            return
        self.matrix[self.line_forklift][self.column_forklift] = constants.EMPTY
        self.line_forklift -= 1;
        self.matrix[self.line_forklift][self.column_forklift] = constants.FORKLIFT

    def move_right(self) -> None:
        if not self.can_move_right():
            return
        self.matrix[self.line_forklift][self.column_forklift] = constants.EMPTY
        self.column_forklift += 1
        self.matrix[self.line_forklift][self.column_forklift] = constants.FORKLIFT

    def move_down(self) -> None:
        if not self.can_move_down():
            return
        self.matrix[self.line_forklift][self.column_forklift] = constants.EMPTY
        self.line_forklift += 1;
        self.matrix[self.line_forklift][self.column_forklift] = constants.FORKLIFT

    def move_left(self) -> None:
        if not self.can_move_left():
            return
        self.matrix[self.line_forklift][self.column_forklift] = constants.EMPTY
        self.column_forklift -= 1
        self.matrix[self.line_forklift][self.column_forklift] = constants.FORKLIFT

    def get_cell_color(self, row: int, column: int) -> Color:
        if row == self.line_exit and column == self.column_exit and (
                row != self.line_forklift or column != self.column_forklift):
            return constants.COLOREXIT

        if self.matrix[row][column] == constants.PRODUCT_CATCH:
            return constants.COLORSHELFPRODUCTCATCH

        if self.matrix[row][column] == constants.PRODUCT:
            return constants.COLORSHELFPRODUCT

        switcher = {
            constants.FORKLIFT: constants.COLORFORKLIFT,
            constants.SHELF: constants.COLORSHELF,
            constants.EMPTY: constants.COLOREMPTY
        }
        return switcher.get(self.matrix[row][column], constants.COLOREMPTY)

    def __str__(self):
        matrix_string = str(self.rows) + " " + str(self.columns) + "\n"
        for row in self.matrix:
            for column in row:
                matrix_string += str(column) + " "
            matrix_string += "\n"
        return matrix_string

    def __eq__(self, other):
        if isinstance(other, WarehouseState):
            return np.array_equal(self.matrix, other.matrix)
        return NotImplemented

    def __hash__(self):
        return hash(self.matrix.tostring())
