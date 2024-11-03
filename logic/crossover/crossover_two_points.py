import copy
import random
from logic.crossover.crossover_algorithm import CrossoverAlgorithm


class CrossoverTwoPoints(CrossoverAlgorithm):
    def cross(self, parent1, parent2):
        if not self.should_cross():
            return []

        child1, child2 = copy.deepcopy(parent1), copy.deepcopy(parent2)
        for chromosome1, chromosome2 in zip(child1.chromosomes, child2.chromosomes):
            gen_list1, gen_list2 = chromosome1.gen_list, chromosome2.gen_list
            if len(gen_list1) != len(gen_list2):
                raise Exception("Chromosomes should have the same number of gens.")

            crossing_points = [random.randint(0, len(gen_list1)) for _ in range(2)]
            crossing_points.sort()
            gen_list1[crossing_points[0]:crossing_points[1]], gen_list2[crossing_points[0]:crossing_points[1]] = \
                gen_list2[crossing_points[0]:crossing_points[1]], gen_list1[crossing_points[0]:crossing_points[1]]
            chromosome1.gen_list = gen_list1
            chromosome2.gen_list = gen_list2
        return child1, child2
