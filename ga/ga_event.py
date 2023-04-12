
from ga.individual import Individual


class GAEvent:

    def __init__(self, best: Individual, average_fitness: float, run_ended: bool = False):
        self.best = best
        self.average_fitness = average_fitness
        self.run_ended = run_ended
