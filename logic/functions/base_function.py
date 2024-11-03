from abc import ABC, abstractmethod


class BaseFunction(ABC):
    @classmethod
    @property
    @abstractmethod
    def NUM_OF_VARIABLES(cls):
        pass

    @abstractmethod
    def evaluate(self, variables):
        pass
