import random
from logic.population import Population
from logic.chromosome import Chromosome
from logic.candidate import Candidate


class Generator:
    @staticmethod
    def generate_random_population(size, range_from, range_to, num_of_genes, fitness_function):
        if range_from > range_to:
            range_from, range_to = range_to, range_from

        population = Population()

        for _ in range(size):
            candidate = Generator.generate_random_candidate(num_of_genes, range_from, range_to, fitness_function)
            population.add_candidate(candidate)

        return population

    @staticmethod
    def generate_random_candidate(num_of_genes, range_from, range_to, fitness_function):
        chromosomes = []
        for _ in range(fitness_function.NUM_OF_VARIABLES):
            chromosomes.append(Generator.generate_random_chromosome(num_of_genes, range_from, range_to))

        return Candidate(chromosomes, fitness_function)

    @staticmethod
    def generate_random_chromosome(num_of_genes, range_from, range_to):
        return Chromosome([random.uniform(range_from, range_to) for _ in range(num_of_genes)], range_from, range_to)
