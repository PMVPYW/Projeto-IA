import copy

import numpy as np
from PIL.ImageEnhance import Color
from numpy import ndarray

import constants
from agentsearch.state import State
from agentsearch.action import Action

from Projeto.warehouse.cell import Cell


class WarehouseState(State[Action]):  # podemos adicionar/alterar métodos

    def __init__(self, matrix: ndarray, rows, columns, forklift_line: int = None, forklift_col: int= None):
        super().__init__()
        # TODO //ver puzzle8
        # //question --> agent can be in exit cell?

        self.rows = rows
        self.columns = columns
        self.matrix = np.copy(matrix)  # np.full([self.rows, self.columns], fill_value=0, dtype=int)

        self.line_forklift = forklift_line
        self.column_forklift = forklift_col

        # possivel otimizar(dá pontos)

        if self.line_forklift is None or self.column_forklift is None:
            for i in range(self.rows):
                if constants.EXIT in self.matrix[i] or constants.FORKLIFT in self.matrix[i]:
                    for j in range(self.columns):
                        # self.matrix[i][j] = matrix[i][j] //removed
                        if self.matrix[i][j] == constants.FORKLIFT:
                            self.line_forklift = i
                            self.column_forklift = j
                        if self.matrix[i][j] == constants.EXIT:
                            self.line_exit = i
                            self.column_exit = j
        else:
            for i in range(self.rows):
                if constants.EXIT in self.matrix[i]:
                    for j in range(self.columns):
                        # self.matrix[i][j] = matrix[i][j] //removed
                        if self.matrix[i][j] == constants.EXIT:
                            self.line_exit = i
                            self.column_exit = j

    def can_move_up(self) -> bool:
        return self.line_forklift != 0 and self.matrix[self.line_forklift - 1][self.column_forklift] == constants.EMPTY

    def can_move_right(self) -> bool:
        return self.column_forklift != self.columns - 1 and self.matrix[self.line_forklift][self.column_forklift + 1] == constants.EMPTY

    def can_move_down(self) -> bool:
        return self.line_forklift != self.rows - 1 and self.matrix[self.line_forklift + 1][self.column_forklift] == constants.EMPTY

    def can_move_left(self) -> bool:
        return self.column_forklift != 0 and self.matrix[self.line_forklift][self.column_forklift - 1] == constants.EMPTY

    def move_up(self) -> None:
        #print(f"UP({self.line_forklift},   {self.column_forklift}) --> ", end="")
        self.matrix[self.line_forklift][self.column_forklift] = constants.EMPTY
        self.line_forklift -= 1;
        self.matrix[self.line_forklift][self.column_forklift] = constants.FORKLIFT
        #print(f"{self.line_forklift},   {self.column_forklift})")

    def move_right(self) -> None:
        #print(f"RIGHT({self.line_forklift},   {self.column_forklift}) --> ", end="")
        self.matrix[self.line_forklift][self.column_forklift] = constants.EMPTY
        self.column_forklift += 1
        self.matrix[self.line_forklift][self.column_forklift] = constants.FORKLIFT
        #print(f"{self.line_forklift},   {self.column_forklift})")

    def move_down(self) -> None:
        #print(f"DOWN({self.line_forklift},   {self.column_forklift}) --> ", end="")
        self.matrix[self.line_forklift][self.column_forklift] = constants.EMPTY
        self.line_forklift += 1;
        self.matrix[self.line_forklift][self.column_forklift] = constants.FORKLIFT
        #print(f"{self.line_forklift},   {self.column_forklift})")

    def move_left(self) -> None:
        #print(f"LEFT({self.line_forklift},   {self.column_forklift}) --> ", end="")
        self.matrix[self.line_forklift][self.column_forklift] = constants.EMPTY
        self.column_forklift -= 1
        self.matrix[self.line_forklift][self.column_forklift] = constants.FORKLIFT
        #print(f"{self.line_forklift},   {self.column_forklift})")

    def get_cell_color(self, row: int, column: int) -> Color:
        if self.matrix[row][column] == constants.EXIT:
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
