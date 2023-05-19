import random

from ga.problem import Problem
from warehouse.warehouse_agent_search import WarehouseAgentSearch
from warehouse.warehouse_individual import WarehouseIndividual


class WarehouseProblemGA(Problem):
    def __init__(self, agent_search: WarehouseAgentSearch):
        # TODO
        self.forklifts = agent_search.forklifts
        self.products = agent_search.products
        self.agent_search = agent_search

    def generate_individual(self) -> "WarehouseIndividual":
        new_individual = WarehouseIndividual(self, len(self.agent_search.pairs))
        new_individual.genome = []
        for i in range(new_individual.num_genes):
            new_individual.genome.append(self.forklifts[random.randint(0, len(self.forklifts))]) #TODO --> Check with teacher
        #genome = wich forklift corresponds to a pair
        '''
        genome size = len(pairs)
        each position as a forklift
        '''
        return new_individual

    def __str__(self):
        string = "# of forklifts: "
        string += f'{len(self.forklifts)}'
        string = "# of products: "
        string += f'{len(self.products)}'
        return string

