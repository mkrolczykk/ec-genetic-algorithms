from logic.population.chromosome import Chromosome
from logic.functions.griewank_function import GriewankFunction
from logic.functions.test_function import TestFunction


def main():

    num_variables = 5
    bit_length = 25
    min_value = -10
    max_value = 10
    population_size = 20


    chromosomes = [Chromosome(num_variables, bit_length, min_value, max_value) for _ in range(population_size)]


    griewank_function = GriewankFunction()


    for i, chrom in enumerate(chromosomes, 1):
        real_values = chrom.decode()
        fitness_value = griewank_function.fitness(real_values)
        print(f"Osobnik {i}:")
        print(f"Reprezentacja binarna: {chrom.get_binary_representation()}")
        print(f"Zdekodowane wartości: {real_values}")
        print(f"Fitness: {fitness_value}\n")

if __name__ == '__main__':
    main()