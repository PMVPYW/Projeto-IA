
from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation
from ga.genetic_algorithm import GeneticAlgorithm


class MutationInsert(Mutation):
    def __init__(self, probability):
        super().__init__(probability)


    def mutate(self, ind: IntVectorIndividual) -> None:
        num_genes = len(ind.genome)
        cut1 = GeneticAlgorithm.rand.randint(0, num_genes - 1)
        cut2 = cut1
        while (cut1 == cut2):
            cut2 = GeneticAlgorithm.rand.randint(0, num_genes - 1)

        if cut1 > cut2:
            cut1, cut2 = cut2, cut1

        mid = int(cut1 + ((cut2 + 1) - cut1) / 2)
        endCount = cut2

        for i in range(cut1, mid):
            aux = ind.genome[i]
            ind.genome[i] = ind.genome[endCount]
            ind.genome[endCount] = aux
            endCount -= 1


    def __str__(self):
        return "Insert Mutation (" + f'{self.probability}' + ")"
