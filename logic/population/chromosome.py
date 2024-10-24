import numpy as np

class Chromosome:
    def __init__(self, num_variables, bit_length, min_value, max_value):
        self.num_variables = num_variables
        self.bit_length = bit_length
        self.min_value = min_value
        self.max_value = max_value
        self.genes = np.random.randint(2, size=(num_variables, bit_length))

    def get_binary_representation(self):
        return self.genes

    def decode(self):
        decoded_values = []
        for gene in self.genes:
            binary_value = int("".join(map(str, gene)), 2)
            #a + decimal(bin) * (b-a)/(2^m - 1)
            real_value = self.min_value + (binary_value / (2 ** self.bit_length - 1)) * (
                        self.max_value - self.min_value)
            decoded_values.append(real_value)
        return decoded_values



