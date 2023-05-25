import copy

import numpy as np

from ga.individual_int_vector import IntVectorIndividual
from warehouse.cell import Cell
from warehouse.pair import Pair


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)


    def compute_fitness(self) -> float:
        products = self.problem.products
        # TODO - Alterar genoma para identificar apenas o produto a fazer pick e humano tem de procurar melhor par
        fitness = 0
        last_pos = self.problem.forklifts[0]
        for i in range(len(self.genome)):
            end_point = products[self.genome[i] - 1]
            fitness += self.get_pair_value(last_pos, end_point)
            last_pos = products[self.genome[i] - 1]
        #saida
        last_pos = products[self.genome[-1] - 1]
        end_point = self.problem.exit
        fitness += self.get_pair_value(last_pos, end_point)
        self.fitness = fitness
        return fitness


    def get_pair_value(self, start: Cell, end: Cell):
        for x in self.problem.agent_search.pairs:
            if (x.cell1 == start and x.cell2 == end) or (x.cell2 == start and x.cell1 == end): #TODO --> check if i can go back (in the path[second if])
                return x.cost

    def obtain_all_path(self):
        # TODO --> check
        path = []
        for pair in self.problem.agent_search.pairs:
            for action in pair.solution.actions:
                print(action)
                path.append(pair.solution.problem)

    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += str(self.genome) + "\n\n"
        # TODO
        return string

    def better_than(self, other: "WarehouseIndividual") -> bool:
        return True if self.fitness < other.fitness else False

    # __deepcopy__ is implemented here so that all individuals share the same problem instance
    def __deepcopy__(self, memo):
        new_instance = self.__class__(self.problem, self.num_genes)
        new_instance.genome = copy.copy(self.genome) #TODO --> check if deepcopy (becomes slower)
        new_instance.fitness = self.fitness
        # TODO
        #new_instance.problem = copy.deepcopy(self.problem)
        return new_instance
