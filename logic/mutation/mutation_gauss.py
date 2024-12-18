import random
from logic.mutation.mutation_algorithm import MutationAlgorithm
from logic.candidate import Candidate


class MutationGauss(MutationAlgorithm):
    def __init__(self, probability, mean=0, stddev=1):
        super().__init__(probability)
        self.mean = mean
        self.stddev = stddev

    def mutate(self, candidate: Candidate):
        if not self.should_mutate():
            return candidate

        for chromosome in candidate.chromosomes:
            for i in range(len(chromosome.gen_list)):
                if random.random() < self.probability:
                    mutation = random.gauss(self.mean, self.stddev)
                    new_value = chromosome.gen_list[i] + mutation
                    chromosome.gen_list[i] = min(max(new_value, chromosome.range_from), chromosome.range_to)

        return candidate
