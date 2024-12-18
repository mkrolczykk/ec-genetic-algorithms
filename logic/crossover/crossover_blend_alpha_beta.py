import copy
import random

from logic.crossover.crossover_algorithm import CrossoverAlgorithm
from logic.candidate import Candidate


class CrossoverBlendAlphaBeta(CrossoverAlgorithm):
    def __init__(self, probability, alpha=0.5, beta=0.5):
        super().__init__(probability)
        self.alpha = alpha
        self.beta = beta

    def cross(self, parent1: Candidate, parent2: Candidate):
        if not self.should_cross():
            return []

        child1, child2 = copy.deepcopy(parent1), copy.deepcopy(parent2)
        for chromosome1, chromosome2 in zip(child1.chromosomes, child2.chromosomes):
            gen_list1 = chromosome1.gen_list
            gen_list2 = chromosome2.gen_list
            chromosome1.gen_list = [
                x + random.uniform(-self.alpha, self.beta) * (y - x) for x, y in zip(gen_list1, gen_list2)
            ]
            chromosome2.gen_list = [
                y + random.uniform(-self.alpha, self.beta) * (x - y) for x, y in zip(gen_list1, gen_list2)
            ]

        return child1, child2
