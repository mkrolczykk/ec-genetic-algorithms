import math
from logic.functions.base_function import BaseFunction


class EggholderFunction(BaseFunction):

    @property
    def NUM_OF_VARIABLES(self):
        return self._NUM_OF_VARIABLES

    @NUM_OF_VARIABLES.setter
    def NUM_OF_VARIABLES(self, value):
        self._NUM_OF_VARIABLES = value

    def __init__(self, num_of_variables):
        if num_of_variables < 2:
            raise ValueError("Eggholder function requires at least 2 variables.")
        self.NUM_OF_VARIABLES = num_of_variables

    def evaluate(self, variables):
        if len(variables) != self.NUM_OF_VARIABLES:
            raise Exception("Function takes {} arguments, but {} were given."
                            .format(self.NUM_OF_VARIABLES, len(variables)))

        total = 0
        for i in range(self.NUM_OF_VARIABLES - 1):
            x = variables[i]
            y = variables[i + 1]

            a = math.sqrt(math.fabs(y + x / 2 + 47))
            b = math.sqrt(math.fabs(x - (y + 47)))

            # calculate Eggholder value for each pair
            total += -(y + 47) * math.sin(a) - x * math.sin(b)

        return total
