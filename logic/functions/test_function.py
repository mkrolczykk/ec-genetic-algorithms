from logic.functions.base_function import BaseFunction


class TestFunction(BaseFunction):
    # sample func, minimum = 0 in (0, 0)

    NUM_OF_VARIABLES = 2

    def evaluate(self, variables):
        if len(variables) != TestFunction.NUM_OF_VARIABLES:
            raise Exception("Function takes {} arguments, but {} were given."
                            .format(TestFunction.NUM_OF_VARIABLES, len(variables)))
        x, y = variables

        return x * x + y * y
