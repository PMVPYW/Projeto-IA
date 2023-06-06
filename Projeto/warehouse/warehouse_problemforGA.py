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
        self.exit = agent_search.exit

    def generate_individual(self) -> "WarehouseIndividual":
        return WarehouseIndividual(self, len(self.products) + len(self.forklifts) - 1)

    def __str__(self):
        string = "# of forklifts: "
        string += f'{len(self.forklifts)}\n'
        string += "# of products: "
        string += f'{len(self.products)}\n'
        string += f'Items\nPath\tCost\n'
        for x in self.agent_search.pairs:
            string += f'{x}\n'
        return string
