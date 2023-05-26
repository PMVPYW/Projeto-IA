import random
from abc import abstractmethod
from ga.problem import Problem
from ga.individual import Individual
import numpy as np

class IntVectorIndividual(Individual):

    def __init__(self, problem: Problem, num_genes: int):
        super().__init__(problem, num_genes)
        self.genome = np.full(num_genes, 0, dtype=int)
        forks = 0
        for i in range(self.num_genes):
            already_in_genome = True
            while already_in_genome:
                already_in_genome = False
                rdn = random.randint(0, self.num_genes)

                already_in_genome = np.isin(rdn, self.genome)

                if rdn == 0:
                    already_in_genome = True
                    if forks < len(self.problem.forklifts):
                        self.genome[i] = -forks
                        forks += 1
                        break

                if not already_in_genome:
                    self.genome[i] = rdn

    def swap_genes(self, other, index: int):
        aux = self.genome[index]
        self.genome[index] = other.genome[index]
        other.genome[index] = aux

    @abstractmethod
    def compute_fitness(self) -> float:
        pass

    @abstractmethod
    def better_than(self, other: "IntVectorIndividual") -> bool:
        pass
