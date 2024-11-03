import statistics


class Population:
    def __init__(self):
        self.__candidates = []

    @property
    def candidates(self):
        return self.__candidates

    @property
    def size(self):
        return len(self.candidates)

    def __str__(self):
        return "\n".join("{}. {}".format(i + 1, candidate) for i, candidate in enumerate(self.candidates))

    def add_candidate(self, candidate):
        self.candidates.append(candidate)

    def get_best_candidate(self, maximization=False):
        return self.get_n_best_candidates(maximization=maximization)[0]

    def get_n_best_candidates(self, n=1, maximization=False):
        return sorted(self.candidates, key=lambda candidate: candidate.score, reverse=maximization)[:n]

    def get_average_score(self):
        return statistics.mean([candidate.score for candidate in self.candidates])

    def get_standard_deviation(self):
        return statistics.stdev([candidate.score for candidate in self.candidates])
