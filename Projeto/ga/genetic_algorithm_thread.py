
import threading
import copy
from ga.genetic_algorithm import GeneticAlgorithm
from ga.genetic_operators.mutation import Mutation
from ga.selection_methods.selection_method import SelectionMethod
from ga.genetic_operators.recombination import Recombination
from ga.ga_event import GAEvent


class GeneticAlgorithmThread(GeneticAlgorithm, threading.Thread):

    def __init__(self,
                 seed: int,
                 population_size: int,
                 max_generations: int,
                 selection_method: SelectionMethod,
                 recombination: Recombination,
                 mutation: Mutation):
        GeneticAlgorithm.__init__(
            self,
            seed,
            population_size,
            max_generations,
            selection_method,
            recombination,
            mutation)
        threading.Thread.__init__(self)
        self.tkinter_listeners = []

    def stop(self) -> None:
        super().stop()

    def run(self):
        super().run()

    # Listeners

    def add_tkinter_listener(self, tkinter_listener):
        self.tkinter_listeners.append(tkinter_listener)

    def fire_generation_ended(self) -> None:
        super().fire_generation_ended()
        for listener in self.tkinter_listeners:
            listener.queue.put(GAEvent(copy.deepcopy(self.best_in_run), self.population.average_fitness))

    def fire_run_ended(self) -> None:
        super().fire_run_ended()
        for listener in self.tkinter_listeners:
            listener.queue.put(GAEvent(copy.deepcopy(self.best_in_run), self.population.average_fitness, True))
