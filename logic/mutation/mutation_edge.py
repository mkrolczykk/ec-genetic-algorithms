import random
from logic.mutation.mutation_algorithm import MutationAlgorithm
from logic.candidate import Candidate


class MutationEdge(MutationAlgorithm):
    def mutate(self, candidate: Candidate):
        if not self.should_mutate():
            return candidate

        for chromosome in candidate.chromosomes:
            num_of_bit = random.randint(0, len(chromosome.gen_list) - 1)
            chromosome.gen_list[num_of_bit] = 1 - chromosome.gen_list[num_of_bit]

        return candidate
