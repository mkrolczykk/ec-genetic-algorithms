import random
import time
from threading import Thread

from pubsub import pub

from logic.algorithm_options import AlgorithmOptions
from logic.functions.functions_factory import FunctionsFactory
from logic.selection.selection_factory import SelectionFactory
from logic.crossover.crossover_factory import CrossoverFactory
from logic.mutation.mutation_factory import MutationFactory
from logic.inversion.inversion import Inversion
from logic.generator import Generator
from logic.population import Population
from other.events.event_algorithm_completed import EventAlgorithmCompleted


class Algorithm(Thread):
    def __init__(self, options: AlgorithmOptions):
        super().__init__()
        self.options = options

    def run(self):
        fitness_function = FunctionsFactory.create(self.options)
        selection_method = SelectionFactory.create(self.options)
        crossover_method = CrossoverFactory.create(self.options)
        mutation_method = MutationFactory.create(self.options)
        inversion_method = Inversion(self.options.inversion_probability)

        execution_time = time.time()
        generations = [Generator.generate_random_population(self.options.population_size,
                                                            self.options.range_from,
                                                            self.options.range_to,
                                                            self.options.precision,
                                                            fitness_function)]
        self.print_statistics(generations[0], with_candidates=False)

        for epoch in range(self.options.epochs_amount):
            generations.append(self.create_next_generation(generations[-1], selection_method, crossover_method,
                                                           mutation_method, inversion_method))

        self.print_statistics(generations[-1], with_candidates=False)
        execution_time = time.time() - execution_time
        time_finished = time.strftime("%Y-%m-%d_%H-%M-%S")

        pub.sendMessage(
            EventAlgorithmCompleted.__name__,
            event=EventAlgorithmCompleted(generations, execution_time, time_finished, self.options)
        )

    def create_next_generation(self, population, selection, crossover, mutation, inversion):
        new_population = Population()
        elite = population.get_n_best_candidates(self.options.elite_strategy_amount, self.options.maximization)
        for candidate in elite:
            new_population.add_candidate(candidate)

        selected_candidates = selection.calculate(population)
        if len(selected_candidates) < 2:
            raise Exception("Less than 2 candidates were selected")

        while new_population.size < population.size:
            parents = random.sample(selected_candidates, 2)
            children = crossover.cross(*parents)
            for child in children:
                if new_population.size >= population.size:
                    break

                mutation.mutate(child)
                inversion.inverse(child)
                new_population.add_candidate(child)

        return new_population

    def print_statistics(self, population, with_candidates=False):
        if with_candidates:
            print("All candidates:")
            print(population)
        print("Best candidate: {}".format(population.get_best_candidate(self.options.maximization)))
        print("Average score: {}".format(population.get_average_score()))
        print("Standard deviation: {}".format(population.get_standard_deviation()))
