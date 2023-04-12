
from agentsearch.action import Action
from warehouse.warehouse_state import WarehouseState


class ActionUp(Action[WarehouseState]):

    def __init__(self):
        Action.__init__(self, 1)

    def execute(self, state: WarehouseState) -> None:
        state.move_up()
        state.action = self

    def is_valid(self, state: WarehouseState) -> bool:
        return state.can_move_up()

    def __str__(self):
        return "UP"


class ActionRight(Action[WarehouseState]):

    def __init__(self):
        Action.__init__(self, 1)

    def execute(self, state: WarehouseState) -> None:
        state.move_right()
        state.action = self

    def is_valid(self, state: WarehouseState) -> bool:
        return state.can_move_right()

    def __str__(self):
        return "RIGHT"


class ActionDown(Action[WarehouseState]):

    def __init__(self):
        Action.__init__(self, 1)

    def execute(self, state: WarehouseState) -> None:
        state.move_down()
        state.action = self

    def is_valid(self, state: WarehouseState) -> bool:
        return state.can_move_down()

    def __str__(self):
        return "DOWN"


class ActionLeft(Action[WarehouseState]):

    def __init__(self):
        Action.__init__(self, 1)

    def execute(self, state: WarehouseState) -> None:
        state.move_left()
        state.action = self

    def is_valid(self, state: WarehouseState) -> bool:
        return state.can_move_left()

    def __str__(self):
        return "LEFT"
