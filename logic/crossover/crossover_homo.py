import copy
from logic.crossover.crossover_algorithm import CrossoverAlgorithm


class CrossoverHomo(CrossoverAlgorithm):
    def cross(self, parent1, parent2):
        child1, child2 = copy.deepcopy(parent1), copy.deepcopy(parent2)
        for chromosome1, chromosome2 in zip(child1.chromosomes, child2.chromosomes):
            gen_list1, gen_list2 = chromosome1.gen_list, chromosome2.gen_list
            if len(gen_list1) != len(gen_list2):
                raise Exception("Chromosomes should have the same number of gens.")

            for i in range(len(gen_list1)):
                if self.should_cross():
                    gen_list1[i], gen_list2[i] = gen_list2[i], gen_list1[i]

            chromosome1.gen_list = gen_list1
            chromosome2.gen_list = gen_list2
        return child1, child2
