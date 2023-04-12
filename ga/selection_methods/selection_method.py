
from abc import ABC, abstractmethod
from ga.population import Population


class SelectionMethod(ABC):

    @abstractmethod
    def run(self, population: Population) -> Population:
        pass
