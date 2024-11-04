from strenum import StrEnum
from enum import auto

from logic.selection.selection_algorithm import SelectionAlgorithm
from logic.selection.selection_best import SelectionBest
from logic.selection.selection_roulette import SelectionRoulette
from logic.selection.selection_tournament import SelectionTournament


class SelectionMethod(StrEnum):
    BEST = auto()
    TOURNAMENT = auto()
    ROULETTE = auto()


class SelectionFactory:
    @staticmethod
    def create(options) -> SelectionAlgorithm:
        match options.selection_method:
            case SelectionMethod.BEST:
                return SelectionBest(options.selection_param, options.maximization)
            case SelectionMethod.ROULETTE:
                return SelectionRoulette(options.selection_param, options.maximization)
            case SelectionMethod.TOURNAMENT:
                return SelectionTournament(options.selection_param, options.maximization)
            case _:
                raise Exception("")
