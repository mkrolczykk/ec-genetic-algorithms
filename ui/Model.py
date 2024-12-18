from automapper import mapper

from logic.algorithm import Algorithm
from logic.algorithm_options import AlgorithmOptions


class Model:
    def __init__(self):
        self.__fitness_function = None
        self.__number_of_variables = None
        self.__range_from = None
        self.__range_to = None
        self.__population_size = None
        self.__precision = None
        self.__epochs_amount = None
        self.__grain_size = None
        self.__elite_strategy_amount = None
        self.__crossover_probability = None
        self.__crossover_alpha = None
        self.__crossover_beta = None
        self.__mutation_probability = None
        self.__inversion_probability = None
        self.__selection_method = None
        self.__selection_param = None
        self.__crossover_method = None
        self.__mutation_method = None
        self.__maximization = None

    @property
    def fitness_function(self):
        return self.__fitness_function

    @fitness_function.setter
    def fitness_function(self, value):
        if not True:
            raise ValueError("")

        self.__fitness_function = value

    @property
    def number_of_variables(self):
        return self.__number_of_variables

    @number_of_variables.setter
    def number_of_variables(self, value):
        if value != int(value) or value < 2:
            raise ValueError("")

        self.__number_of_variables = value

    @property
    def range_from(self):
        return self.__range_from

    @range_from.setter
    def range_from(self, value):
        if value != float(value):
            raise ValueError("")

        self.__range_from = value

    @property
    def range_to(self):
        return self.__range_to

    @range_to.setter
    def range_to(self, value):
        if value != float(value):
            raise ValueError("")

        self.__range_to = value

    @property
    def population_size(self):
        return self.__population_size

    @population_size.setter
    def population_size(self, value):
        if value != int(value) or value < 2:
            raise ValueError("")

        self.__population_size = value

    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, value):
        if value != int(value) or value < 0:
            raise ValueError("")

        self.__precision = value

    @property
    def epochs_amount(self):
        return self.__epochs_amount

    @epochs_amount.setter
    def epochs_amount(self, value):
        if value != int(value) or value < 0:
            raise ValueError("")

        self.__epochs_amount = value

    @property
    def grain_size(self):
        return self.__grain_size

    @grain_size.setter
    def grain_size(self, value):
        if value != int(value) or value < 2:
            raise ValueError("")

        self.__grain_size = value

    @property
    def elite_strategy_amount(self):
        return self.__elite_strategy_amount

    @elite_strategy_amount.setter
    def elite_strategy_amount(self, value):
        if value != int(value) or value < 0:
            raise ValueError("")

        self.__elite_strategy_amount = value

    @property
    def crossover_probability(self):
        return self.__crossover_probability

    @crossover_probability.setter
    def crossover_probability(self, value):
        if value != int(value) or value <= 0:
            raise ValueError("")

        self.__crossover_probability = value

    @property
    def crossover_alpha(self):
        return self.__crossover_alpha

    @crossover_alpha.setter
    def crossover_alpha(self, value):
        if value != float(value) or value <= 0 or value > 1:
            raise ValueError("Crossover alpha must be a float between 0 and 1")

        self.__crossover_alpha = value

    @property
    def crossover_beta(self):
        return self.__crossover_beta

    @crossover_beta.setter
    def crossover_beta(self, value):
        if value != float(value) or value <= 0 or value > 1:
            raise ValueError("Crossover beta must be a float between 0 and 1")

        self.__crossover_beta = value

    @property
    def mutation_probability(self):
        return self.__mutation_probability

    @mutation_probability.setter
    def mutation_probability(self, value):
        if value != int(value) or value < 0:
            raise ValueError("")

        self.__mutation_probability = value

    @property
    def inversion_probability(self):
        return self.__inversion_probability

    @inversion_probability.setter
    def inversion_probability(self, value):
        if value != int(value) or value < 0:
            raise ValueError("")

        self.__inversion_probability = value

    @property
    def selection_method(self):
        return self.__selection_method

    @selection_method.setter
    def selection_method(self, value):
        if not True:
            raise ValueError("")

        self.__selection_method = value

    @property
    def selection_param(self):
        return self.__selection_param

    @selection_param.setter
    def selection_param(self, value):
        if value != int(value):
            raise ValueError("")

        self.__selection_param = value

    @property
    def crossover_method(self):
        return self.__crossover_method

    @crossover_method.setter
    def crossover_method(self, value):
        if not True:
            raise ValueError("")

        self.__crossover_method = value

    @property
    def mutation_method(self):
        return self.__mutation_method

    @mutation_method.setter
    def mutation_method(self, value):
        if not True:
            raise ValueError("")

        self.__mutation_method = value

    @property
    def maximization(self):
        return self.__maximization

    @maximization.setter
    def maximization(self, value):
        if value != bool(value):
            raise ValueError("")

        self.__maximization = value

    def run_algorithm(self):
        options = mapper.to(AlgorithmOptions).map(self)
        algorithm_thread = Algorithm(options)
        algorithm_thread.start()
