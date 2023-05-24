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
        # TODO - Alterar genoma para identificar apenas o produto a fazer pick e humano tem de procurar melhor par
        m_v = self.get_max_value()
        last_pos = self.problem.forklifts[0]
        self.fitness = 0
        for i in self.genome:
            b_pair = self.best_pair(i, last_pos)
            if b_pair is None:
                self.fitness += m_v
            else:
                last_pos = b_pair.cell2
                self.fitness += b_pair.cost


        # penalization for missing numbers
        missing = 1  # starts 1 because it will be the exp. of missing
        for i in range(1, len(self.problem.products)):
            if not np.isin(i, self.genome):
                print(f"###{i}")
                self.fitness += m_v

        # add cost to exit
        exit_path = self.obter_saida(last_pos)
        if exit_path != None:
            self.fitness += exit_path.cost
        else:
            self.fitness *= 1.5

        return self.fitness

    def obter_saida(self, last_pos: Cell):
        exit = self.problem.exit
        for x in self.problem.agent_search.pairs:
            if x.cell2.line == exit.line and x.cell2.column == exit.column and x.cell1.line == last_pos.line and x.cell1.column == last_pos.column:
                return x

    def best_pair(self, pick: int, lastPos: Cell) -> Pair:
        b_p = None
        pk = self.problem.products[pick - 1]
        for x in self.problem.agent_search.pairs:
            if x.cell2.line == pk.line and x.cell2.column == pk.column \
                    and x.cell1.line == lastPos.line and x.cell1.column == lastPos.column:
                b_p = x
                break
        return b_p

    def obtain_all_path(self):
        # TODO --> check
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
