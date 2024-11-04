import math
from logic.functions.base_function import BaseFunction


class SchafferTwoFunction(BaseFunction):
    # minimum = 0 at (0, 0), range [-100, 100], maximum = 1 in (+-1.25313, +-1.25313)

    NUM_OF_VARIABLES = 2

    def evaluate(self, variables):
        if len(variables) != SchafferTwoFunction.NUM_OF_VARIABLES:
            raise Exception("Function takes {} arguments, but {} were given."
                            .format(SchafferTwoFunction.NUM_OF_VARIABLES, len(variables)))
        x, y = variables

        numerator = math.sin(x ** 2 - y ** 2) ** 2 - 0.5
        denominator = (1 + 0.001 * (x ** 2 + y ** 2)) ** 2

        return 0.5 + numerator / denominator
