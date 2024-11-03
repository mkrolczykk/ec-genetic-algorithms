import random
from abc import ABC, abstractmethod


class CrossoverAlgorithm(ABC):
    def __init__(self, probability):
        self.probability = probability / 100

    def should_cross(self):
        return random.random() < self.probability

    @abstractmethod
    def cross(self, parent1, parent2):
        pass
