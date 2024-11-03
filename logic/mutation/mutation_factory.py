from logic.algorithm_options import AlgorithmOptions
from logic.mutation.mutation_algorithm import MutationAlgorithm
from logic.mutation.mutation_method import MutationMethod
from logic.mutation.mutation_one_point import MutationOnePoint
from logic.mutation.mutation_two_points import MutationTwoPoints


class MutationFactory:
    @staticmethod
    def create(options: AlgorithmOptions) -> MutationAlgorithm:
        match options.mutation_method:
            case MutationMethod.ONE_POINT:
                return MutationOnePoint(options.mutation_probability)
            case MutationMethod.TWO_POINTS:
                return MutationTwoPoints(options.mutation_probability)
            case _:
                raise Exception("")
