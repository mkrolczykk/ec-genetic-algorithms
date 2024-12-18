from strenum import StrEnum
from enum import auto

from logic.crossover.crossover_algorithm import CrossoverAlgorithm
from logic.crossover.crossover_one_point import CrossoverOnePoint
from logic.crossover.crossover_two_points import CrossoverTwoPoints
from logic.crossover.crossover_granular import CrossoverGranular
from logic.crossover.crossover_homo import CrossoverHomo
from logic.crossover.crossover_arithmetic import CrossoverArithmetic
from logic.crossover.crossover_linear import CrossoverLinear
from logic.crossover.crossover_blend_alpha import CrossoverBlendAlpha
from logic.crossover.crossover_blend_alpha_beta import CrossoverBlendAlphaBeta
from logic.crossover.crossover_averaging import CrossoverAveraging


class CrossoverMethod(StrEnum):
    # ONE_POINT = auto()
    # TWO_POINTS = auto()
    # GRANULAR = auto()
    # HOMO = auto()
    ARITHMETIC = auto()
    LINEAR = auto()
    BLEND_ALPHA = auto()
    BLEND_ALPHA_BETA = auto()
    AVERAGING = auto()


class CrossoverFactory:
    @staticmethod
    def create(options) -> CrossoverAlgorithm:
        match options.crossover_method:
            # case CrossoverMethod.ONE_POINT:
            #     return CrossoverOnePoint(options.crossover_probability)
            # case CrossoverMethod.TWO_POINTS:
            #     return CrossoverTwoPoints(options.crossover_probability)
            # case CrossoverMethod.GRANULAR:
            #     return CrossoverGranular(options.crossover_probability, options.grain_size)
            # case CrossoverMethod.HOMO:
            #     return CrossoverHomo(options.crossover_probability)
            case CrossoverMethod.ARITHMETIC:
                return CrossoverArithmetic(options.crossover_probability)
            case CrossoverMethod.LINEAR:
                return CrossoverLinear(options.crossover_probability)
            case CrossoverMethod.BLEND_ALPHA:
                return CrossoverBlendAlpha(options.crossover_probability, options.crossover_alpha)
            case CrossoverMethod.BLEND_ALPHA_BETA:
                return CrossoverBlendAlphaBeta(options.crossover_probability, options.crossover_alpha, options.crossover_beta)
            case CrossoverMethod.AVERAGING:
                return CrossoverAveraging(options.crossover_probability)
            case _:
                raise Exception("")
