import random

from logic.candidate import Candidate


class Inversion:
    def __init__(self, probability):
        self.probability = probability / 100

    def should_inverse(self):
        return random.random() < self.probability

    def inverse(self, candidate: Candidate):
        if not self.should_inverse():
            return candidate

        for chromosome in candidate.chromosomes:
            inversion_range = [random.randint(0, len(chromosome.gen_list) - 1) for _ in range(2)]
            inversion_range.sort()
            start, end = inversion_range
            chromosome.gen_list[start:end + 1] = list(reversed(chromosome.gen_list[start:end + 1]))

        return candidate
