import random
from individual import Individual
from selection import Selection
from crossover import Crossover
from mutation import Mutation
from inversion import Inversion
from elitysm import apply_elitism

class Population:
    def __init__(self, size, chromosome_length, lower_bound, upper_bound, bit_length, value_range):
        # Konstruktor klasy Population tworzy początkową populację osobników
        self.individuals = [
            Individual(chromosome_length * bit_length, value_range[0], value_range[1]) for _ in range(size)
        ]

    def evaluate_fitness(self, mode):
        # Metoda evaluate_fitness oblicza wartość przystosowania dla wszystkich osobników w populacji
        for individual in self.individuals:
            individual.evaluate_fitness(mode)

    def select_parents(self, selection_method):
        # Metoda select_parents wybiera rodziców do krzyżowania w zależności od wybranej metody selekcji
        return Selection.select(self.individuals, selection_method)

    def crossover(self, parents, crossover_type):
        # Metoda crossover stosuje krzyżowanie na rodzicach w celu stworzenia dzieci
        return Crossover.apply(parents, crossover_type)

    def mutate_population(self, mutation_rate, mutation_type):
        # Metoda mutate_population stosuje mutację na całej populacji
        Mutation.apply(self.individuals, mutation_rate, mutation_type)

    def apply_inversion(self, inversion_rate):
        # Metoda apply_inversion stosuje operator inwersji na całej populacji
        Inversion.apply(self.individuals, inversion_rate)

    def generate_next_population(self, mutation_rate, mutation_type, crossover_type, elitism_rate, inversion_rate, selection_method):
        # Metoda generate_next_population tworzy nową populację, wykorzystując elityzm, selekcję, krzyżowanie, mutację i inwersję
        # Elityzm - najlepsze osobniki przechodzą bez zmian do kolejnej populacji
        next_population = apply_elitism(self.individuals, elitism_rate)

        # Tworzenie nowych osobników poprzez selekcję i krzyżowanie
        while len(next_population) < len(self.individuals):
            parents = self.select_parents(selection_method)
            child1, child2 = self.crossover(parents, crossover_type)
            next_population.extend([child1, child2])

        # Mutacja i inwersja nowej populacji
        self.mutate_population(mutation_rate, mutation_type)
        self.apply_inversion(inversion_rate)

        self.individuals = next_population

