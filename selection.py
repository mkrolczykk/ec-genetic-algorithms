import random

class Selection:
    @staticmethod
    def select(individuals, method):
        # Metoda select wybiera rodziców do krzyżowania w zależności od wybranej metody selekcji
        if method == 'tournament':
            # Selekcja turniejowa: losowo wybieramy kilku osobników i wybieramy najlepszego z nich
            tournament_size = 3
            best = random.choice(individuals)
            for _ in range(tournament_size - 1):
                contender = random.choice(individuals)
                if contender.fitness < best.fitness:
                    best = contender
            return best, random.choice(individuals)
        elif method == 'roulette':
            # Selekcja koła ruletki: osobniki są wybierane z prawdopodobieństwem proporcjonalnym do ich przystosowania
            max_fitness = sum(ind.fitness for ind in individuals)
            pick = random.uniform(0, max_fitness)
            current = 0
            for ind in individuals:
                current += ind.fitness
                if current > pick:
                    return ind, random.choice(individuals)
        elif method == 'best':
            # Selekcja najlepszych: wybieramy dwóch najlepszych osobników
            sorted_individuals = sorted(individuals, key=lambda ind: ind.fitness)
            return sorted_individuals[0], sorted_individuals[1]
