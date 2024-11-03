import random
from abc import ABC, abstractmethod
from logic.candidate import Candidate


class MutationAlgorithm(ABC):
    def __init__(self, probability):
        self.probability = probability / 100

    def should_mutate(self):
        return random.random() < self.probability

    @abstractmethod
    def mutate(self, candidate: Candidate):
        pass
