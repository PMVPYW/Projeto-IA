import copy

import numpy as np

from ga.individual_int_vector import IntVectorIndividual
from warehouse.cell import Cell
from warehouse.pair import Pair


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        self.fitness = None

    def get_max_value(self):
        m = 0
        for x in self.problem.agent_search.pairs:
            m += x.cost
        return m

    def compute_fitness(self) -> float:
        print(self.genome)
        max_value = self.get_max_value()
        # TODO - Alterar genoma para identificar apenas o produto a fazer pick e humano tem de procurar melhor par
        last_pos = self.problem.forklifts[0]
        used = []
        self.fitness = 0
        e = 0
        for i in self.genome:
            if i != 0 and i % len(self.problem.products) == 0:
                exit_pair = self.obter_saida(last_pos)
                if exit_pair is None:
                    self.fitness *= 2
                else:
                    self.fitness += exit_pair.cost
                last_pos = self.problem.forklifts[i // len(self.problem.products) - 1]
            if i == 0:
                continue
            b_pair = self.best_pair(i, last_pos)
            if b_pair is not None:
                last_pos = b_pair.cell2
                self.fitness += b_pair.cost
            else:
                self.fitness *= 2
            e += 1
        # obter melhor saida
        exit_pair = self.obter_saida(last_pos)
        if exit_pair is None:
            self.fitness *= 2
        else:
            self.fitness += exit_pair.cost

        # check if there are all numbers
        for x in range(1, len(self.problem.products) + 1):
            if not np.isin(x, self.genome):
                self.fitness += max_value/len(self.problem.products)
        return self.fitness

    def obter_saida(self, last_pos: Cell):
        exit = self.problem.exit
        for x in self.problem.agent_search.pairs:
            if x.cell2.line == exit.line and x.cell2.column == exit.column and x.cell1.line == last_pos.line and x.cell1.column == last_pos.column:
                return x

    def best_pair(self, pick: int, last_pos: Cell) -> Pair:
        b_p = None
        i = 0
        pk = self.problem.products[pick - 1]
        for x in self.problem.agent_search.pairs:
            if x.cell2.line == pk.line and x.cell2.column == pk.column \
                    and x.cell1.line == last_pos.line and x.cell1.column == last_pos.column:
                b_p = x
                break
        return b_p

    def obtain_all_path(self):
        # TODO --> needs to be changed
        path = []
        for i in range(self.num_genes):
            if self.genome[i]:
                path.append(self.problem.agent_search.pairs[i].solution.get_path())
        for x in path:
            print("p", end="")
            for i in x:
                print(i, end=" ")
            print("\n")
        return path, 3

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
        new_instance.genome = copy.deepcopy(self.genome)
        new_instance.fitness = self.fitness
        # TODO
        new_instance.problem = copy.deepcopy(self.problem)
        return new_instance
