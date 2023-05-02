from random import random

from ga.individual import Individual
from ga.genetic_operators.recombination import Recombination

class Recombination2(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        if random.random() < self.probability:
            length = min(len(ind1.genotype), len(ind2.genotype))
            if length < 2:
                return

            # Choose two random crossover points
            pt1, pt2 = sorted(random.sample(range(length), 2))

            # Swap the genetic material between the two points
            ind1.genotype[pt1:pt2], ind2.genotype[pt1:pt2] = ind2.genotype[pt1:pt2], ind1.genotype[pt1:pt2]

    def __str__(self):
        return "Recombination 2 (" + f'{self.probability}' + ")"
