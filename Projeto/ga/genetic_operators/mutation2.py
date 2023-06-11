import random

from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation


class Mutation2(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:  # mutação de troca (troca 2 elementos) #TODO --> check if can use
        elem1 = random.randint(0, len(ind.genome) - 1)
        elem2 = elem1
        while elem1 == elem2:
            elem2 = random.randint(0, len(ind.genome) - 1)

        aux = ind.genome[elem1]
        ind.genome[elem1] = ind.genome[elem2]
        ind.genome[elem2] = aux

    def __str__(self):
        return "Mutation 2 (" + f'{self.probability}' + ")"
