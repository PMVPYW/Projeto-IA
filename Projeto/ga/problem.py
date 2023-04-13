
from abc import ABC, abstractmethod
from ga.individual import Individual


class Problem(ABC):

    @abstractmethod
    def generate_individual(self) -> Individual:
        pass
