import random
from logic.mutation.mutation_algorithm import MutationAlgorithm
from logic.candidate import Candidate


class MutationEven(MutationAlgorithm):
    def mutate(self, candidate: Candidate):
        if not self.should_mutate():
            return candidate

        for chromosome in candidate.chromosomes:
            for i in range(len(chromosome.gen_list)):
                if random.random() < self.probability:
                    chromosome.gen_list[i] = random.uniform(chromosome.range_from, chromosome.range_to)

        return candidate
