from strenum import StrEnum
from enum import auto
from logic.algorithm_options import AlgorithmOptions
from logic.functions.base_function import BaseFunction
from logic.functions.eggholder_function import EggholderFunction
from logic.functions.griewank_function import GriewankFunction
from logic.functions.schaffer_two_function import SchafferTwoFunction
from logic.functions.test_function import TestFunction


class FitnessFunction(StrEnum):
    EGGHOLDER_FUNCTION = auto()
    GRIEWANK_FUNCTION = auto()
    SCHAFFER_N2_FUNCTION = auto()
    TEST_FUNCTION = auto()


class FunctionsFactory:
    @staticmethod
    def create(options: AlgorithmOptions) -> BaseFunction:
        match options.fitness_function:
            case FitnessFunction.EGGHOLDER_FUNCTION:
                return EggholderFunction(options.number_of_variables)
            case FitnessFunction.GRIEWANK_FUNCTION:
                return GriewankFunction(options.number_of_variables)
            case FitnessFunction.SCHAFFER_N2_FUNCTION:
                return SchafferTwoFunction()
            case FitnessFunction.TEST_FUNCTION:
                return TestFunction()
            case _:
                raise Exception("")
