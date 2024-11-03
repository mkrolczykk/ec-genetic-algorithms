from abc import ABC, abstractmethod


class SelectionAlgorithm(ABC):
    def __init__(self, maximization=False):
        self.maximization = maximization

    @abstractmethod
    def calculate(self, population):
        pass
