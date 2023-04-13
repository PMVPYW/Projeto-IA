
import os
import numpy as np
from ga.ga_listener import GAListener
from ga.ga_event import GAEvent
from experiments.experiment_listener import ExperimentListener
from experiments.experiment_event import ExperimentEvent


class StatisticBestAverage(GAListener, ExperimentListener):

    def __init__(self, num_runs: int, experiment_header: str):
        self.values = np.full(num_runs, 0, dtype=float)
        self.run = 0
        if not os.path.isfile('statistic_average_fitness.xls'):
            with open('statistic_average_fitness.xls', 'a+') as file:
                file.write(experiment_header + '\t' + 'Average:' + '\t' + 'StdDev:' + '\n')

    def generation_ended(self, ga_event: GAEvent) -> None:
        pass

    def run_ended(self, ga_event: GAEvent) -> None:
        self.values[self.run] = ga_event.best.fitness
        self.run += 1
        print(ga_event.best.fitness)

    def experiment_ended(self, experiment_event: ExperimentEvent) -> None:
        average = np.average(self.values)
        sd = np.std(self.values)
        with open('statistic_average_fitness.xls', 'a') as file:
            file.write(experiment_event.experiment.experiment_values + '\t' + str(average) + '\t' + str(sd) + '\n')
