
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from agentsearch.state import State

P = TypeVar("P", bound="Problem")
S = TypeVar("S", bound=State)


class Heuristic(ABC, Generic[P, S]):

    def __init__(self):
        self._problem = None

    @abstractmethod
    def compute(self, state: S) -> float:
        pass

    @property
    def problem(self):
        return self._problem

    @problem.setter
    def problem(self, problem: P):
        self._problem = problem
