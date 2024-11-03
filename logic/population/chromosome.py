import math


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
        self.__gen_list = value

    @property
    def range_from(self):
        return self.__range_from

    @range_from.setter
    def range_from(self, value):
        if value != float(value):
            raise ValueError("Given value should be float.")
        self.__range_from = value

    @property
    def range_to(self):
        return self.__range_to

    @range_to.setter
    def range_to(self, value):
        if value != float(value):
            raise ValueError("Given value should be float.")
        self.__range_to = value

    @property
    def num_of_bits(self):
        return len(self.__gen_list)

    def __str__(self):
        return "".join([str(x) for x in self.gen_list])

    def decode_to_decimal(self):
        binary_str = ''.join([str(x) for x in self.gen_list])
        decimal_num = int(binary_str, 2)

        return self.range_from + decimal_num * (self.range_to - self.range_from) / (pow(2, self.num_of_bits) - 1)

    @staticmethod
    def calculate_num_of_bits(range_from, range_to, precision):
        return math.ceil(math.log2((range_to - range_from) * pow(10, precision) + 1))