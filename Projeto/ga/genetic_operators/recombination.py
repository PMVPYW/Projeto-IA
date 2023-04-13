
from abc import abstractmethod
from ga.individual import Individual
from ga.genetic_operators.genetic_operator import GeneticOperator
from ga.population import Population
from ga.genetic_algorithm import GeneticAlgorithm


class Recombination(GeneticOperator):

    def __init__(self, probability: float):
        super().__init__(probability)

    def run(self, population: Population) -> None:
        i = 0
        while i < population.size:
            if GeneticAlgorithm.rand.random() < self.probability:
                self.recombine(population.individuals[i], population.individuals[i + 1])
            i += 2

    @abstractmethod
    def recombine(self, ind1: Individual, ind2: Individual):
        pass
