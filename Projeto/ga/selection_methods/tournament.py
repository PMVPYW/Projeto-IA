
import copy
from ga.genetic_algorithm import GeneticAlgorithm
from ga.population import Population
from ga.selection_methods.selection_method import SelectionMethod
from ga.individual import Individual


class Tournament(SelectionMethod):

    def __init__(self, tournament_size: int):
        self.tournament_size = tournament_size

    def run(self, population: Population) -> Population:
        new_population = Population(population.size)
        for i in range(population.size):
            new_population.individuals.append(self.tournament(population))
        return new_population

    def tournament(self, population: Population) -> Individual:
        best = population.individuals[GeneticAlgorithm.rand.randint(0, population.size - 1)]
        for i in range(1, self.tournament_size):
            ind = population.individuals[GeneticAlgorithm.rand.randint(0, population.size - 1)]
            if ind.better_than(best):
                best = ind
        return copy.deepcopy(best)

    def __str__(self):
        return "Tournament selection(" + f'{self.tournament_size}' + ")"


