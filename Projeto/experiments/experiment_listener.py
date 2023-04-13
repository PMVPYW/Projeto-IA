
from abc import ABC, abstractmethod
from experiments.experiment_event import ExperimentEvent


class ExperimentListener(ABC):

    @abstractmethod
    def experiment_ended(self, experiment_event: ExperimentEvent) -> None:
        pass

