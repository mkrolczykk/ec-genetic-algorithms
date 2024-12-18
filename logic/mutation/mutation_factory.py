from strenum import StrEnum
from enum import auto
from logic.mutation.mutation_algorithm import MutationAlgorithm
from logic.mutation.mutation_edge import MutationEdge
from logic.mutation.mutation_one_point import MutationOnePoint
from logic.mutation.mutation_two_points import MutationTwoPoints
from logic.mutation.mutation_even import MutationEven
from logic.mutation.mutation_gauss import MutationGauss


class MutationMethod(StrEnum):
    # ONE_POINT = auto()
    # TWO_POINTS = auto()
    # EDGE = auto()
    EVEN = auto()
    GAUSS = auto()


class MutationFactory:
    @staticmethod
    def create(options) -> MutationAlgorithm:
        match options.mutation_method:
            # case MutationMethod.ONE_POINT:
            #     return MutationOnePoint(options.mutation_probability)
            # case MutationMethod.TWO_POINTS:
            #     return MutationTwoPoints(options.mutation_probability)
            # case MutationMethod.EDGE:
            #     return MutationEdge(options.mutation_probability)
            case MutationMethod.EVEN:
                return MutationEven(options.mutation_probability)
            case MutationMethod.GAUSS:
                return MutationGauss(options.mutation_probability)
            case _:
                raise Exception("")
