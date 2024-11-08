import random
from logic.mutation.mutation_algorithm import MutationAlgorithm
from logic.candidate import Candidate


class MutationEdge(MutationAlgorithm):
    def mutate(self, candidate: Candidate):
        if not self.should_mutate():
            return candidate

        for chromosome in candidate.chromosomes:
            if random.random() < 0.5:
                chromosome.gen_list[0] = 1 - chromosome.gen_list[0]
            else:
                chromosome.gen_list[-1] = 1 - chromosome.gen_list[-1]

        return candidate
