import math
from logic.functions.base_function import BaseFunction


class GriewankFunction(BaseFunction):

    @property
    def NUM_OF_VARIABLES(self):
        return self._NUM_OF_VARIABLES

    @NUM_OF_VARIABLES.setter
    def NUM_OF_VARIABLES(self, value):
        self._NUM_OF_VARIABLES = value

    def __init__(self, num_of_variables):
        if num_of_variables < 1:
            raise ValueError("Griewank function requires at least 1 variable.")
        self.NUM_OF_VARIABLES = num_of_variables

    def evaluate(self, variables):
        if len(variables) != self.NUM_OF_VARIABLES:
            raise Exception("Function takes {} arguments, but {} were given."
                            .format(self.NUM_OF_VARIABLES, len(variables)))

        sum_part = sum((x ** 2) / 4000 for x in variables)
        product_part = math.prod(math.cos(x / math.sqrt(i + 1)) for i, x in enumerate(variables))

        return sum_part - product_part + 1
