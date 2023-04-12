
from abc import ABC, abstractmethod
from ga.ga_event import GAEvent


class GAListener(ABC):

    @abstractmethod
    def generation_ended(self, ga_event: GAEvent) -> None:
        pass

    @abstractmethod
    def run_ended(self, ga_event: GAEvent) -> None:
        pass

