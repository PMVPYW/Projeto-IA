
from abc import ABC, abstractmethod
from ga.population import Population


class GeneticOperator(ABC):

    def __init__(self, probability: float):
        self.probability = probability

    @abstractmethod
    def run(self, population: Population) -> None:
        pass
