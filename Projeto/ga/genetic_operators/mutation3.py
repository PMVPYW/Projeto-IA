import copy
import random

from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation


class Mutation3(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:  # shift mutation #TODO --> check if can use
        gen = copy.deepcopy(ind.genome)
        len_gen = len(ind.genome)
        shift_value = random.randint(1, len_gen - 1)

        for i in range(len_gen):
            ind.genome[i] = gen[(i + shift_value) % len_gen]

    def __str__(self):
        return "Mutation 3 (" + f'{self.probability}' + ")"
