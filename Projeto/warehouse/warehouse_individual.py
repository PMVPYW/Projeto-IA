import copy

import numpy as np

from ga.individual_int_vector import IntVectorIndividual
from warehouse.cell import Cell
from warehouse.pair import Pair


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)


    def compute_fitness(self) -> float:
        not_reached = [x for x in range(1, len(self.problem.products)+1)]
        products = self.problem.products
        # TODO - Alterar genoma para identificar apenas o produto a fazer pick e humano tem de procurar melhor par
        if (self.genome[2] == -2):
            a = 0
        fitness = 0
        forklift_index = 0
        max_forklift_index = len(self.problem.forklifts)
        last_pos = self.problem.forklifts[forklift_index]
        for i in range(len(self.genome)):
            if self.genome[i] < 1:
                end_point = self.problem.exit
                fitness += self.get_pair_value(last_pos, end_point)
                forklift_index += 1
                if not forklift_index < max_forklift_index:
                    # penalizar por não ir a pontos
                    missing = len(not_reached) + 1
                    fitness **= missing
                    self.fitness = fitness
                    return fitness
                last_pos = self.problem.forklifts[forklift_index]
                continue
            end_point = products[self.genome[i] - 1]
            fitness += self.get_pair_value(last_pos, end_point)
            last_pos = products[self.genome[i] - 1]
            not_reached.remove(self.genome[i])
        #saida
        last_pos = products[self.genome[-1] - 1]
        end_point = self.problem.exit
        fitness += self.get_pair_value(last_pos, end_point)

        #penalizar por não ir a pontos
        missing =  len(not_reached) + 1
        fitness **= missing

        self.fitness = fitness
        return fitness



    def get_pair_value(self, start: Cell, end: Cell):
        for x in self.problem.agent_search.pairs:
            if (x.cell1 == start and x.cell2 == end) or (x.cell2 == start and x.cell1 == end): #TODO --> check if i can go back (in the path[second if])
                return x.cost

    def get_pair_path(self, start: Cell, end: Cell):
        for x in self.problem.agent_search.pairs:
            if (x.cell1 == start and x.cell2 == end):
                return x.get_path()
            elif (x.cell2 == start and x.cell1 == end):
                return x.get_path()[::-1]
    def obtain_all_path(self):
        # TODO --> check
        path = []
        steps = 0
        forklift_index = 0
        max_forklift_index = len(self.problem.forklifts)
        products = self.problem.products
        last_pos = self.problem.forklifts[forklift_index]
        partial_path = [last_pos]
        for i in range(len(self.genome)):
            if self.genome[i] < 1 :
                end_point = self.problem.exit
                partial_path += self.get_pair_path(last_pos, end_point)
                partial_path.append(end_point)
                forklift_index += 1
                if not forklift_index < max_forklift_index:
                    break
                path.append(partial_path)
                last_pos = self.problem.forklifts[forklift_index]
                steps = max(steps, len(partial_path))
                partial_path = [last_pos]

            end_point = products[self.genome[i] - 1]
            partial_path += self.get_pair_path(last_pos, end_point)
            last_pos = products[self.genome[i] - 1]
        path.append(partial_path)
        steps = max(steps, len(partial_path))
        return path, steps

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
