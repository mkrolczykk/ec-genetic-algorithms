import random
from individual import Individual

class Crossover:
    @staticmethod
    def apply(parents, crossover_type):
        # Metoda apply stosuje krzyżowanie na rodzicach, w zależności od wybranego typu krzyżowania
        if crossover_type == 'one_point':
            # Krzyżowanie jednopunktowe: jedno miejsce cięcia w chromosomie
            crossover_point = random.randint(0, len(parents[0].chromosome.genes) - 1)
            child1_genes = parents[0].chromosome.genes[:crossover_point] + parents[1].chromosome.genes[crossover_point:]
            child2_genes = parents[1].chromosome.genes[:crossover_point] + parents[0].chromosome.genes[crossover_point:]
            child1 = Individual(len(child1_genes), parents[0].lower_bound, parents[0].upper_bound)
            child2 = Individual(len(child2_genes), parents[1].lower_bound, parents[1].upper_bound)
            return child1, child2
        elif crossover_type == 'two_point':
            # Krzyżowanie dwupunktowe: dwa miejsca cięcia w chromosomie
            point1 = random.randint(0, len(parents[0].chromosome.genes) - 1)
            point2 = random.randint(point1, len(parents[0].chromosome.genes) - 1)
            child1_genes = parents[0].chromosome.genes[:point1] + parents[1].chromosome.genes[point1:point2] + parents[0].chromosome.genes[point2:]
            child2_genes = parents[1].chromosome.genes[:point1] + parents[0].chromosome.genes[point1:point2] + parents[1].chromosome.genes[point2:]
            child1 = Individual(len(child1_genes), parents[0].lower_bound, parents[0].upper_bound)
            child2 = Individual(len(child2_genes), parents[1].lower_bound, parents[1].upper_bound)
            return child1, child2
        elif crossover_type == 'uniform':
            # Krzyżowanie jednorodne: każdy gen jest losowo wybierany od jednego z rodziców
            child1_genes = []
            child2_genes = []
            for gene1, gene2 in zip(parents[0].chromosome.genes, parents[1].chromosome.genes):
                if random.random() < 0.5:
                    child1_genes.append(gene1)
                    child2_genes.append(gene2)
                else:
                    child1_genes.append(gene2)
                    child2_genes.append(gene1)
            child1 = Individual(len(child1_genes), parents[0].lower_bound, parents[0].upper_bound)
            child2 = Individual(len(child2_genes), parents[1].lower_bound, parents[1].upper_bound)
            return child1, child2