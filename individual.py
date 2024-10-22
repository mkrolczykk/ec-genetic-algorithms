from chromosome import Chromosome
from fitness_function import griewank_function

class Individual:
    def __init__(self, chromosome_length, lower_bound, upper_bound):
        # Konstruktor klasy Individual tworzy osobnika z chromosomem o określonej długości
        self.chromosome = Chromosome(chromosome_length)
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.fitness = None

    def evaluate_fitness(self, mode):
        # Metoda evaluate_fitness oblicza wartość przystosowania na podstawie funkcji celu
        real_value = self.chromosome.get_real_value(self.lower_bound, self.upper_bound)
        self.fitness = griewank_function([real_value])
        # Dopasowanie wartości przystosowania w zależności od trybu (minimalizacja lub maksymalizacja)
        if mode == "minimize":
            self.fitness = -self.fitness
        elif mode == "maximize":
            self.fitness = self.fitness

    def mutate(self, mutation_rate):
        # Metoda mutate wywołuje mutację chromosomu osobnika
        self.chromosome.mutate(mutation_rate)
