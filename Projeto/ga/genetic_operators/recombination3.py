from ga.genetic_operators.recombination import Recombination
from ga.individual import Individual

class Recombination3(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        # TODO
        pass

    def __str__(self):
        return "Recombination 3 (" + f'{self.probability}' + ")"