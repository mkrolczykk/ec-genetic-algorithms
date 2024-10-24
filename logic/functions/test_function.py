from .base_function import BaseFunction

class TestFunction(BaseFunction):
    def calculate_fitness(self, real_values):
        test = 2 * real_values[0] ** 2 + 5
        return test
