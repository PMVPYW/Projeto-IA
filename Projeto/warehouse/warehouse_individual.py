import copy

from ga.individual_int_vector import IntVectorIndividual


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        self.fitness = None


    def compute_fitness(self) -> float:
        # TODO - Check with teacher
        '''
        idea --> get sum of all path costs, and find the difference betwen that and the current path
        if 2 forklifts are to the same pick, there is a penalization that is half of the 2º path costs
        '''
        self.fitness = 0
        max = 0
        atributed_picks = []
        for i in range(self.num_genes):
            if self.genome[i]:
                self.fitness += self.problem.agent_search.pairs[i].cost
                if (self.problem.agent_search.pairs[i].cell2 in atributed_picks):
                    self.fitness -= self.problem.agent_search.pairs[i].cost
                else:
                    atributed_picks.append(self.problem.agent_search.pairs[i].cell2)
            max += self.problem.agent_search.pairs[i].cost
        self.fitness = max - self.fitness
        return self.fitness


    def obtain_all_path(self):
        # TODO
        pass

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
