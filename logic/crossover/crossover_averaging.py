import copy

from logic.crossover.crossover_algorithm import CrossoverAlgorithm
from logic.candidate import Candidate


class CrossoverAveraging(CrossoverAlgorithm):
    def cross(self, parent1: Candidate, parent2: Candidate):
        if not self.should_cross():
            return []

        child1, child2 = copy.deepcopy(parent1), copy.deepcopy(parent2)
        for chromosome1, chromosome2 in zip(child1.chromosomes, child2.chromosomes):
            gen_list1 = chromosome1.gen_list
            gen_list2 = chromosome2.gen_list
            average = [(x + y) / 2 for x, y in zip(gen_list1, gen_list2)]
            chromosome1.gen_list = average
            chromosome2.gen_list = average

        return child1, child2
