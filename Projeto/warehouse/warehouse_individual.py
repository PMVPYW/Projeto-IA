import copy

import numpy as np
import statistics as stats

from ga.individual_int_vector import IntVectorIndividual
from warehouse.cell import Cell


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        self.paths = None
        self.steps = None
        self.targets = None
        self.fitness = None

    def compute_fitness(self) -> float:
        products = self.problem.products
        num_prods = len(products)
        fitness = 0
        forklift_index = 0
        max_forklift_index = len(self.problem.forklifts)
        forklift_costs = [0 for x in range(max_forklift_index)]
        last_pos = self.problem.forklifts[forklift_index]
        for gene in self.genome:
            if gene > num_prods:
                end_point = self.problem.exit
                fitness += self.get_pair_value(last_pos, end_point)
                forklift_costs[forklift_index] = fitness
                fitness = 0
                forklift_index += 1
                last_pos = self.problem.forklifts[forklift_index]
                continue
            end_point = products[gene - 1]
            fitness += self.get_pair_value(last_pos, end_point)
            last_pos = products[gene - 1]
        end_point = self.problem.exit
        fitness += self.get_pair_value(last_pos, end_point)
        forklift_costs[forklift_index] = fitness
        self.fitness = sum(forklift_costs)
        self.fitness += (self.getColisionsNumber() * 100)  # 100 points by colision
        self.fitness *= max(forklift_costs)
        '''fitness = sum(forklift_costs)
        if (max_forklift_index == 1):
            fitness *= (1 + stats.stdev(forklift_costs))'''

        return fitness


def getColisionsNumber(self) -> int:
    colisions = 0
    if len(self.problem.forklifts) == 1:
        return 0
    # colisões nos cruzamentos
    paths, steps, targets = self.obtain_all_path()
    paths = copy.deepcopy(paths)

    for path in paths:
        while len(path) != steps:
            path.append(None)

    # deteção em cruzamentos

    colisions += self.count_crossway_colisions(paths)

    print("Colisions: ", colisions)
    return colisions


def count_crossway_colisions(self, paths):
    colisions = 0
    forklift_number = len(self.problem.forklifts)
    current_positions = [None for x in range(forklift_number)]
    for i in range(self.steps):
        for j in range(forklift_number):
            current_positions[j] = paths[j][i]
        cols = 0
        for k in range(forklift_number):
            for h in range(forklift_number):
                if (k != h):
                    cell1 = current_positions[k]
                    cell2 = current_positions[h]
                    if cell1 is None or cell2 is None:
                        continue
                    if cell1.line == cell2.line and cell1.column == cell2.column:
                        cols += 1

        colisions += cols // 2
    return colisions


def prevent_crossway_colision(self, paths, step, forklift_1, forklift_2):
    aux = None


def get_pair_value(self, start: Cell, end: Cell):
    for x in self.problem.agent_search.pairs:
        if (x.cell1 == start and x.cell2 == end) or (x.cell2 == start and x.cell1 == end):
            return x.cost


def get_pair_path(self, start: Cell, end: Cell):
    for x in self.problem.agent_search.pairs:
        if x.cell1 == start and x.cell2 == end:
            return x.path
        elif x.cell2 == start and x.cell1 == end:
            return x.path[::-1]


def obtain_all_path(self):
    if self.paths != None and self.targets != None and self.steps != None:
        return self.paths, self.steps, self.targets
    path = []
    targets = []
    partial_targets = []
    steps = 0
    forklift_index = 0
    max_forklift_index = len(self.problem.forklifts)
    products = self.problem.products
    num_prods = len(products)
    last_pos = self.problem.forklifts[forklift_index]
    partial_path = [last_pos]
    for gene in self.genome:
        if gene > num_prods:
            end_point = self.problem.exit
            partial_path += self.get_pair_path(last_pos, end_point)
            partial_path.append(end_point)
            forklift_index += 1
            if not forklift_index < max_forklift_index:
                break
            path.append(partial_path)
            targets.append(partial_targets)
            partial_targets = []
            last_pos = self.problem.forklifts[forklift_index]
            steps = max(steps, len(partial_path))
            partial_path = [last_pos]
            continue
        end_point = products[gene - 1]
        partial_targets.append(end_point.column)
        partial_path += self.get_pair_path(last_pos, end_point)
        last_pos = products[gene - 1]
    end_point = self.problem.exit
    partial_path += self.get_pair_path(last_pos, end_point)
    partial_path.append(end_point)
    path.append(partial_path)
    targets.append(partial_targets)
    steps = max(steps, len(partial_path))
    self.paths = path
    self.steps = steps
    self.targets = targets
    return path, steps, targets


def __str__(self):
    string = 'Fitness: ' + f'{self.fitness}' + '\n'
    string += str(self.genome) + "\n\n"
    # TODO
    return string


def better_than(self, other: "WarehouseIndividual") -> bool:
    return self.fitness < other.fitness


def __deepcopy__(self, memo):
    new_instance = self.__class__(self.problem, self.num_genes)
    new_instance.genome = copy.copy(self.genome)
    new_instance.fitness = self.fitness
    # TODO
    new_instance.steps = self.steps
    new_instance.paths = self.paths
    new_instance.targets = self.targets
    return new_instance
