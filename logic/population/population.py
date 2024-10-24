from .chromosome import Chromosome

class Population:
    def __init__(self, population_size, num_variables, bit_length, min_value, max_value):
        self.population_size = population_size
        self.chromosomes = [
            Chromosome(num_variables, bit_length, min_value, max_value) for _ in range(population_size)
        ]

    def evaluate_population(self, function):
        fitness_scores = []
        for chromosome in self.chromosomes:
            real_values = chromosome.decode()
            fitness = function.fitness(real_values)
            fitness_scores.append(fitness)
        return fitness_scores


