from logic.chromosome import Chromosome
from logic.functions.base_function import BaseFunction


class Candidate:
    def __init__(self, chromosomes, fitness_function):
        self.chromosomes = chromosomes
        self.fitness_function = fitness_function

    @property
    def chromosomes(self):
        return self.__chromosomes

    @chromosomes.setter
    def chromosomes(self, value):
        if not isinstance(value, list):
            raise ValueError("Given object is not an instance of list.")
        if not all(isinstance(chromosome, Chromosome) for chromosome in value):
            raise ValueError("All elements in chromosomes must be instances of Chromosome.")
        self.__chromosomes = value

    @property
    def fitness_function(self):
        return self.__fitness_function

    @fitness_function.setter
    def fitness_function(self, value):
        if not isinstance(value, BaseFunction):
            raise ValueError("Given object is not an instance of BaseFitnessFunction.")
        self.__fitness_function = value

    @property
    def decoded_chromosomes(self):
        return [chromosome.decode_to_decimal() for chromosome in self.chromosomes]

    @property
    def score(self):
        return self.fitness_function.evaluate(self.decoded_chromosomes)

    def __str__(self):
        return "score = {}, {}".format(self.score, ", ".join(
            ["x{} = {} ({})".format(i, solution, ", ".join(map(str, chromosome.gen_list)))
             for i, (chromosome, solution) in enumerate(zip(self.chromosomes, self.decoded_chromosomes))]))
