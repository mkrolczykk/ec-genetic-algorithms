import copy
import random

from logic.crossover.crossover_algorithm import CrossoverAlgorithm
from logic.candidate import Candidate


class CrossoverOnePoint(CrossoverAlgorithm):
    def cross(self, parent1: Candidate, parent2: Candidate):
        if not self.should_cross():
            return []

        child1, child2 = copy.deepcopy(parent1), copy.deepcopy(parent2)
        for chromosome1, chromosome2 in zip(child1.chromosomes, child2.chromosomes):
            gen_list1, gen_list2 = chromosome1.gen_list, chromosome2.gen_list
            if len(gen_list1) != len(gen_list2):
                raise Exception("Chromosomes should have the same number of gens.")

            crossing_point = random.randint(1, len(gen_list1) - 1)
            gen_list1, gen_list2 = gen_list1[:crossing_point] + gen_list2[crossing_point:], \
                                   gen_list2[:crossing_point] + gen_list1[crossing_point:]
            chromosome1.gen_list = gen_list1
            chromosome2.gen_list = gen_list2
        return child1, child2
