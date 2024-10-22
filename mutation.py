import random

class Mutation:
    @staticmethod
    def apply(individuals, mutation_rate, mutation_type):
        # Metoda apply stosuje mutację na całej populacji, w zależności od wybranego typu mutacji
        for individual in individuals:
            if mutation_type == 'boundary':
                # Mutacja brzegowa: zmiana wartości skrajnych genów
                individual.mutate(mutation_rate)
            elif mutation_type == 'one_point':
                # Mutacja jednopunktowa: losowy jeden gen jest zmieniany
                if random.random() < mutation_rate:
                    mutation_point = random.randint(0, len(individual.chromosome.genes) - 1)
                    individual.chromosome.genes[mutation_point] = 1 if individual.chromosome.genes[mutation_point] == 0 else 0
            elif mutation_type == 'two_point':
                # Mutacja dwupunktowa: dwa losowe geny są zmieniane
                if random.random() < mutation_rate:
                    point1 = random.randint(0, len(individual.chromosome.genes) - 1)
                    point2 = random.randint(point1, len(individual.chromosome.genes) - 1)
                    for i in range(point1, point2 + 1):
                        individual.chromosome.genes[i] = 1 if individual.chromosome.genes[i] == 0 else 0
