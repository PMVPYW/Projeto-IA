
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

S = TypeVar("S", bound='State')


class Action(ABC, Generic[S]):

    def __init__(self, cost):
        self.cost = cost

    @abstractmethod
    def execute(self, state: S) -> None:
        pass

    @abstractmethod
    def is_valid(self, state: S) -> bool:
        pass

