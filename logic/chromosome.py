import random


class Chromosome:
    def __init__(self, gen_list, range_from, range_to):
        self.gen_list = gen_list
        self.range_from = range_from
        self.range_to = range_to

    @property
    def gen_list(self):
        return self.__gen_list

    @gen_list.setter
    def gen_list(self, value):
        if not isinstance(value, list):
            raise ValueError("Given object is not an instance of list.")
        if not all(isinstance(x, (int, float)) for x in value):
            raise ValueError("All genes must be integers or floats.")
        self.__gen_list = value

    @property
    def range_from(self):
        return self.__range_from

    @range_from.setter
    def range_from(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Given value should be a number.")
        self.__range_from = float(value)

    @property
    def range_to(self):
        return self.__range_to

    @range_to.setter
    def range_to(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Given value should be a number.")
        self.__range_to = float(value)

    @property
    def num_of_genes(self):
        return len(self.__gen_list)

    def __str__(self):
        return ", ".join([f"{x:.4f}" for x in self.gen_list])

    def decode_to_decimal(self):

        decimal_value = sum(self.gen_list) / len(self.gen_list)

        return decimal_value

    @staticmethod
    def generate_random_chromosome(length, range_from, range_to):

        return Chromosome(
            gen_list=[random.uniform(range_from, range_to) for _ in range(length)],
            range_from=range_from,
            range_to=range_to
        )

    @staticmethod
    def calculate_precision(range_from, range_to, num_of_genes):

        return abs(range_to - range_from) / num_of_genes
