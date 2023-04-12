
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

A = TypeVar("A", bound="Action")


class State(ABC, Generic[A]):

    def __init__(self):
        self.action = None

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __hash__(self):
        pass
