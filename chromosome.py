import random

class Chromosome:
    def __init__(self, length):
        # Konstruktor klasy Chromosome inicjuje losową sekwencję bitów (genów) o zadanej długości
        self.length = length
        self.genes = [random.choice([0, 1]) for _ in range(length)]

    def mutate(self, mutation_rate):
        # Metoda mutate wprowadza mutacje w genach z zadanym prawdopodobieństwem mutacji
        for i in range(self.length):
            if random.random() < mutation_rate:
                self.genes[i] = 1 if self.genes[i] == 0 else 0

    def get_real_value(self, lower_bound, upper_bound):
        # Metoda get_real_value konwertuje binarną reprezentację na wartość rzeczywistą w zadanym przedziale
        binary_str = "".join(str(g) for g in self.genes)
        decimal_value = int(binary_str, 2)
        return lower_bound + (upper_bound - lower_bound) * (decimal_value / (2**self.length - 1))

