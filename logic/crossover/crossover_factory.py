from logic.algorithm_options import AlgorithmOptions
from logic.crossover.crossover_algorithm import CrossoverAlgorithm
from logic.crossover.crossover_method import CrossoverMethod
from logic.crossover.crossover_one_point import CrossoverOnePoint
from logic.crossover.crossover_two_points import CrossoverTwoPoints
from logic.crossover.crossover_granular import CrossoverGranular
from logic.crossover.crossover_homo import CrossoverHomo


class CrossoverFactory:
    @staticmethod
    def create(options: AlgorithmOptions) -> CrossoverAlgorithm:
        match options.crossover_method:
            case CrossoverMethod.ONE_POINT:
                return CrossoverOnePoint(options.crossover_probability)
            case CrossoverMethod.TWO_POINTS:
                return CrossoverTwoPoints(options.crossover_probability)
            case CrossoverMethod.GRANULAR:
                return CrossoverGranular(options.crossover_probability)
            case CrossoverMethod.HOMO:
                return CrossoverHomo(options.crossover_probability)
            case _:
                raise Exception("")
