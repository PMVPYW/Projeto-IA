
import os
import copy
from ga.ga_listener import GAListener
from ga.ga_event import GAEvent
from experiments.experiment_listener import ExperimentListener
from experiments.experiment_event import ExperimentEvent


class StatisticBestInRun(GAListener, ExperimentListener):

    def __init__(self, experiment_header: str):
        self.experiment_best = None
        if not os.path.isfile('statistic_best_per_experiment_fitness.xls'):
            with open('statistic_best_per_experiment_fitness.xls', 'a+') as file:
                file.write(experiment_header + '\tFitness:' + '\n')

    def generation_ended(self, ga_event: GAEvent) -> None:
        pass

    def run_ended(self, ga_event: GAEvent) -> None:
        if not self.experiment_best or ga_event.best.better_than(self.experiment_best):
            self.experiment_best = copy.deepcopy(ga_event.best)

    def experiment_ended(self, experiment_event: ExperimentEvent) -> None:
        experiment_textual_representation = experiment_event.experiment.experiment_textual_representation
        experiment_configuration_values = experiment_event.experiment.experiment_values

        with open('statistic_best_per_experiment_fitness.xls', 'a+') as file:
            file.write(experiment_configuration_values + '\t' + str(self.experiment_best.fitness) + '\n')

        with open('statistic_best_per_experiment.txt', 'a+') as file:
            file.write('\n' + experiment_textual_representation + str(self.experiment_best))
            file.write('\n\n' + '# --------------------------------------------------------------' + '\n')
