from strenum import StrEnum
from enum import auto


class FitnessFunction(StrEnum):
    EGGHOLDER_FUNCTION = auto()
    GRIEWANK_FUNCTION = auto()
    SCHAFFER_N2_FUNCTION = auto()
    SCHAFFER_N4_FUNCTION = auto()
    TEST_FUNCTION = auto()
    # TODO -> ADD ME
