from strenum import StrEnum
from enum import auto


class CrossoverMethod(StrEnum):
    ONE_POINT = auto()
    TWO_POINTS = auto()
    GRANULAR = auto()
    HOMO = auto()
