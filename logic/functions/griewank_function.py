import numpy as np
from .base_function import BaseFunction

class GriewankFunction(BaseFunction):
    def calculate_fitness(self, real_values):
        Griewank_part_1 = sum([x ** 2 / 4000 for x in real_values])
        Griewank_part_2 = np.prod([np.cos(x / np.sqrt(i + 1)) for i, x in enumerate(real_values)])
        return 1 + Griewank_part_1 - Griewank_part_2
