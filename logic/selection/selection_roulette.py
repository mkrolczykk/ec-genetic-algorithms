from operator import attrgetter
import numpy as np
from logic.selection.selection_algorithm import SelectionAlgorithm


class SelectionRoulette(SelectionAlgorithm):
    def __init__(self, size=3, maximization=False):
        super().__init__(maximization)
        self.__size = size

    def calculate(self, population):
        def fitness(score, maximization): return score if maximization else 1 / score

        candidates = []

        min_candidate = min(population.candidates, key=attrgetter("score"))
        offset = 1 - min_candidate.score if min_candidate.score <= 0 else 0
        fitness_sum = sum([fitness(candidate.score + offset, self.maximization) for candidate in population.candidates])
        probabilities = [fitness(candidate.score + offset, self.maximization) / fitness_sum for candidate in
                         population.candidates]

        for _ in range(self.__size):
            candidates.append(np.random.choice(population.candidates, p=probabilities))

        return candidates
