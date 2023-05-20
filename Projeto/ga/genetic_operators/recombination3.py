from ga.genetic_algorithm import GeneticAlgorithm
from ga.genetic_operators.recombination import Recombination
from ga.individual import Individual

class Recombination3(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None: #recombination_Uniform
        for i in range(ind1.num_genes):
            if GeneticAlgorithm.rand.getrandbits(1) == 1:
                ind1.genome[i], ind2.genome[i] = ind2.genome[i], ind1.genome[i]

    def __str__(self):
        return "Recombination 3 (" + f'{self.probability}' + ")"