
from abc import ABC, abstractmethod
import numpy as np
from experiments.experiment import Experiment
from experiments.parameter import Parameter
from ga.genetic_algorithm import GeneticAlgorithm


class ExperimentsFactory(ABC):

    def __init__(self, filename: str):
        self.num_runs = None
        self.parameters = None
        self.ordered_parameters_array = None
        self.statistics_names = []
        self.statistics = []
        self.read_parameters_file(filename)
        self.read_statistics_file(filename)

    @abstractmethod
    def build_experiment(self) -> Experiment:
        pass

    @abstractmethod
    def generate_ga_instance(self, seed: int) -> GeneticAlgorithm:
        pass

    def has_more_experiments(self) -> bool:
        return self.ordered_parameters_array[0].active_value_index < len(self.ordered_parameters_array[0].values)

    def next_experiment(self) -> Experiment:
        if self.has_more_experiments():
            experiment = self.build_experiment()
            self.indices_managing(self.ordered_parameters_array.size - 1)
            return experiment

    def indices_managing(self, index: int) -> None:
        self.ordered_parameters_array[index].active_value_index += 1
        if index != 0 and \
           self.ordered_parameters_array[index].active_value_index >= len(self.ordered_parameters_array[index].values):
            self.ordered_parameters_array[index].active_value_index = 0
            index -= 1
            self.indices_managing(index)

    def read_parameters_file(self, filename: str) -> None:
        file = open(filename, 'r')
        data = file.readlines()
        lines = []
        for line in data:
            if line and len(line) > 1 and not line.startswith('#') and not line.startswith('Statistic'):
                lines.append(line.strip())
        file.close()

        self.parameters = {}
        self.ordered_parameters_array = np.full(len(lines), fill_value='', dtype=Parameter)

        i = 0
        for line in lines:
            tokens1 = line.split(':')
            parameter_values = []
            parameter_name = tokens1[0].strip()
            tokens2 = tokens1[1].split(',')
            for j in range(0, len(tokens2)):
                parameter_values.append(tokens2[j].strip())

            parameter = Parameter(parameter_name, parameter_values)
            self.parameters[parameter_name] = parameter
            self.ordered_parameters_array[i] = parameter
            i += 1

    def read_statistics_file(self, filename: str) -> None:
        file = open(filename, 'r')
        data = file.readlines()
        for line in data:
            if line and len(line) > 1 and line.startswith('Statistic'):
                tokens = line.split(':')
                self.statistics_names.append(tokens[1].strip())
        file.close()

    def get_parameter_value(self, parameter_name: str) -> str:
        return self.parameters.get(parameter_name).get_active_value()
