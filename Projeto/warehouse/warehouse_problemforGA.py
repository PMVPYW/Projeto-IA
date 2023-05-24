import random

from ga.genetic_algorithm import GeneticAlgorithm
from ga.problem import Problem
from warehouse.warehouse_agent_search import WarehouseAgentSearch
from warehouse.warehouse_individual import WarehouseIndividual


class WarehouseProblemGA(Problem):
    def __init__(self, agent_search: WarehouseAgentSearch):
        # TODO --> check
        self.forklifts = agent_search.forklifts
        self.products = agent_search.products
        self.agent_search = agent_search

    def generate_individual(self) -> "WarehouseIndividual":
        repeated = []
        new_individual = WarehouseIndividual(self, len(self.agent_search.products))
        for i in range(new_individual.num_genes):
            n = GeneticAlgorithm.rand.randint(1, new_individual.num_genes)
            while n in repeated:
                n = GeneticAlgorithm.rand.randint(1, new_individual.num_genes)
            new_individual.genome[i] = n
        # genome = wich forklift corresponds to a pair
        '''
        genome size = len(pairs)
        each position as a pair
        '''
        return new_individual

    def __str__(self):
        string = "# of forklifts: "
        string += f'{len(self.forklifts)}\n'
        string += "# of products: "
        string += f'{len(self.products)}\n'
        string += f'Items\nPath\tCost\n'
        for x in self.agent_search.pairs:
            string += f'{x}\n'
        return string
