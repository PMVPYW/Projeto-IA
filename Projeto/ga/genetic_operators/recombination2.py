from random import random

from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual import Individual
from ga.genetic_operators.recombination import Recombination

class Recombination2(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None: #2 cuts recombination
        cut1 = GeneticAlgorithm.rand.randint(0, ind1.num_genes)
        cut2 = GeneticAlgorithm.rand.randint(0, ind1.num_genes)
        if cut1 > cut2:
            cut1, cut2 = cut2, cut1

        for i in range(cut1, cut2):
            ind1.genome[i], ind2.genome[i] = ind2.genome[i], ind1.genome[i]

    def __str__(self):
        return "Recombination 2 (" + f'{self.probability}' + ")"
