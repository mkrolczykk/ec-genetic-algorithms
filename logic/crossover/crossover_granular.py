import copy
import random
from logic.crossover.crossover_algorithm import CrossoverAlgorithm
from logic.candidate import Candidate


class CrossoverGranular(CrossoverAlgorithm):
    def __init__(self, probability, grain_size: int):
        super().__init__(probability)
        self.grain_size = grain_size  # number of genes in one block to be replaced

    def cross(self, parent1: Candidate, parent2: Candidate):
        if not self.should_cross():
            return []

        child1, child2 = copy.deepcopy(parent1), copy.deepcopy(parent2)

        for chromosome1, chromosome2 in zip(child1.chromosomes, child2.chromosomes):
            gen_list1, gen_list2 = chromosome1.gen_list, chromosome2.gen_list

            if len(gen_list1) != len(gen_list2):
                raise Exception("Chromosomes should have the same number of gens.")

            for i in range(0, len(gen_list1), self.grain_size):
                end = min(i + self.grain_size, len(gen_list1))

                if self.should_cross():
                    gen_list1[i:end], gen_list2[i:end] = gen_list2[i:end], gen_list1[i:end]

            chromosome1.gen_list = gen_list1
            chromosome2.gen_list = gen_list2

        return child1, child2
