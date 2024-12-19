import random
from logic.selection.selection_algorithm import SelectionAlgorithm


class SelectionTournament(SelectionAlgorithm):
    def __init__(self, group_size=3, maximization=False):
        super().__init__(maximization)
        self.group_size = group_size

    def calculate(self, population):
        if len(population.candidates) < 2:
            raise ValueError("Population must contain at least 2 candidates for tournament selection.")

        shuffled_candidates = population.candidates[:]
        random.shuffle(shuffled_candidates)
        selected_candidates = []

        for i in range(0, len(shuffled_candidates), self.group_size):
            group = shuffled_candidates[i:i + self.group_size]
            selected_candidates.append(self.select_best_from_group(group))

        while len(selected_candidates) < 2:
            selected_candidates.append(random.choice(population.candidates))

        return selected_candidates

    def select_best_from_group(self, group):
        return max(group, key=lambda candidate: candidate.score) if self.maximization else min(group, key=lambda candidate: candidate.score)
