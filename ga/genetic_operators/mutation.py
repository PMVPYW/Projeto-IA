
from abc import abstractmethod

from ga.individual import Individual
from ga.genetic_operators.genetic_operator import GeneticOperator
from ga.population import Population
from ga.genetic_algorithm import GeneticAlgorithm

class Mutation(GeneticOperator):

    def __init__(self, probability: float):
        super().__init__(probability)

    def run(self, population: Population) -> None:
        population_size = len(population.individuals)
        for i in range(population_size):
            if GeneticAlgorithm.rand.random() < self.probability:
                self.mutate(population.individuals[i])

    @abstractmethod
    def mutate(self, individual: Individual) -> None:
        pass
