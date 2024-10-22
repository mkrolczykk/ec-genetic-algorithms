import random

class Inversion:
    @staticmethod
    def apply(individuals, inversion_rate):
        # Metoda apply stosuje operator inwersji na całej populacji
        for individual in individuals:
            if random.random() < inversion_rate:
                start = random.randint(0, len(individual.chromosome.genes) - 1)
                end = random.randint(start, len(individual.chromosome.genes) - 1)
                individual.chromosome.genes[start:end+1] = reversed(individual.chromosome.genes[start:end+1])