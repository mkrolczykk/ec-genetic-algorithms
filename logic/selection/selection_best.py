from logic.selection.selection_algorithm import SelectionAlgorithm


class SelectionBest(SelectionAlgorithm):
    def __init__(self, percent=60, maximization=False):
        super().__init__(maximization)
        self.percent = percent

    def calculate(self, population):
        candidates = sorted(population.candidates, key=lambda candidate: candidate.score, reverse=self.maximization)
        return candidates[:int(population.size * self.percent / 100)]
