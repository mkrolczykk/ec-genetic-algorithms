from strenum import StrEnum
from enum import auto
from logic.algorithm_options import AlgorithmOptions
from logic.functions.base_function import BaseFunction
from logic.functions.eggholder_function import EggholderFunction
from logic.functions.griewank_function import GriewankFunction
from logic.functions.schaffer_four_function import SchafferFourFunction
from logic.functions.schaffer_two_function import SchafferTwoFunction
from logic.functions.test_function import TestFunction


class FitnessFunction(StrEnum):
    EGGHOLDER_FUNCTION = auto()
    GRIEWANK_FUNCTION = auto()
    SCHAFFER_N2_FUNCTION = auto()
    SCHAFFER_N4_FUNCTION = auto()
    TEST_FUNCTION = auto()
    # TODO -> ADD ME


class FunctionsFactory:
    @staticmethod
    def create(options: AlgorithmOptions) -> BaseFunction:
        match options.fitness_function:
            case FitnessFunction.EGGHOLDER_FUNCTION:
                return EggholderFunction()
            case FitnessFunction.GRIEWANK_FUNCTION:
                return GriewankFunction()
            case FitnessFunction.SCHAFFER_N2_FUNCTION:
                return SchafferTwoFunction()
            case FitnessFunction.SCHAFFER_N4_FUNCTION:
                return SchafferFourFunction()
            case FitnessFunction.TEST_FUNCTION:
                return TestFunction()
            case _:
                raise Exception("")
