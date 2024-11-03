from logic.algorithm_options import AlgorithmOptions
from logic.selection.selection_algorithm import SelectionAlgorithm
from logic.selection.selection_method import SelectionMethod
from logic.selection.selection_best import SelectionBest
from logic.selection.selection_roulette import SelectionRoulette
from logic.selection.selection_tournament import SelectionTournament


class SelectionMethodFactory:
    @staticmethod
    def create(options: AlgorithmOptions) -> SelectionAlgorithm:
        match options.selection_method:
            case SelectionMethod.BEST:
                return SelectionBest(options.selection_param, options.maximization)
            case SelectionMethod.ROULETTE:
                return SelectionRoulette(options.selection_param, options.maximization)
            case SelectionMethod.TOURNAMENT:
                return SelectionTournament(options.selection_param, options.maximization)
            case _:
                raise Exception("")
