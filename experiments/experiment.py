
from ga.problem import Problem
from experiments.experiment_event import ExperimentEvent


class Experiment:

    def __init__(self, factory: "ExperimentsFactory", num_runs: int, problem: Problem,
                 experiment_textual_representation: str, experiment_header: str, experiment_values: str):
        self.factory = factory
        self.num_runs = num_runs
        self.problem = problem
        self.experiment_textual_representation = experiment_textual_representation
        self.experiment_header = experiment_header
        self.experiment_values = experiment_values
        self.listeners = []

    def run(self):
        for run in range(self.num_runs):
            ga = self.factory.generate_ga_instance(run + 1)
            ga.problem = self.problem
            ga.run()
        self.fire_experiment_ended()

    def __str__(self):
        return self.experiment_textual_representation

    # listeners

    def add_listener(self, listener) -> None:
        if listener not in self.listeners:
            self.listeners.append(listener)

    def fire_experiment_ended(self):
        for listener in self.listeners:
            listener.experiment_ended(ExperimentEvent(self))
