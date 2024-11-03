import random
from logic.selection.selection_algorithm import SelectionAlgorithm


class SelectionTournament(SelectionAlgorithm):
    def __init__(self, group_size=3, maximization=False):
        super().__init__(maximization)
        self.group_size = group_size

    def calculate(self, population):
        random.shuffle(population.candidates)
        candidates = []
        for i in range(0, population.size, self.group_size):
            group = population.candidates[i:i + self.group_size]
            candidates.append(self.select_best_from_group(group))

        return candidates

    def select_best_from_group(self, group):
        sorted_group = sorted(group, key=lambda candidate: candidate.score, reverse=self.maximization)
        return sorted_group[0]
