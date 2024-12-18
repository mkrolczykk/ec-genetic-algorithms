import copy

from logic.crossover.crossover_algorithm import CrossoverAlgorithm
from logic.candidate import Candidate


class CrossoverArithmetic(CrossoverAlgorithm):
    def cross(self, parent1: Candidate, parent2: Candidate):
        if not self.should_cross():
            return []

        child1, child2 = copy.deepcopy(parent1), copy.deepcopy(parent2)
        for chromosome1, chromosome2 in zip(child1.chromosomes, child2.chromosomes):
            chromosome1.gen_list = [(x + y) / 2 for x, y in zip(chromosome1.gen_list, chromosome2.gen_list)]
            chromosome2.gen_list = [(x + y) / 2 for x, y in zip(chromosome2.gen_list, chromosome1.gen_list)]

        return child1, child2
