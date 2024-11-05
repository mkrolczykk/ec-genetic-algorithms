import csv
import pathlib
from pubsub import pub
from other.events.event_algorithm_completed import EventAlgorithmCompleted
from other.events_listeners.event_listener import EventListener


class DataStorageEventListener(EventListener):
    def listen(self):
        pub.subscribe(self.__handle, EventAlgorithmCompleted.__name__)

    @staticmethod
    def __handle(event: EventAlgorithmCompleted):
        dir_path = "output/" + event.time_finished
        pathlib.Path(dir_path).mkdir(parents=True, exist_ok=True)
        DataStorageEventListener.__save_info(dir_path, event.execution_time, event.generations[-1], event.options)

        file_name = dir_path + "/results.csv"
        with open(file_name, "w", encoding="UTF8") as file:
            writer = csv.writer(file)
            writer.writerow(["epoch", "best_solution", "best_score", "average", "std"])

            for epoch, generation in enumerate(event.generations):
                best_candidate = generation.get_best_candidate(maximization=event.options.maximization)
                writer.writerow([epoch,
                                 best_candidate.decoded_chromosomes,
                                 best_candidate.score,
                                 generation.get_average_score(),
                                 generation.get_standard_deviation()])

    @staticmethod
    def __save_info(directory_name, execution_time, last_generation, options):
        info_file_name = directory_name + "/results.txt"
        solution = last_generation.get_best_candidate(maximization=options.maximization)

        values = [chromosome.decode_to_decimal() for chromosome in solution.chromosomes[:options.number_of_variables]]
        values_str = ", ".join(f"{value:.5f}" for value in values)

        with open(info_file_name, "w", encoding="UTF8") as file:
            file.write("Function: {} (maximization? {})\n".format(options.fitness_function, options.maximization))
            file.write(f"f({values_str}) = {solution.score:.5f}\n")
            file.write("Range: [{}, {}]\n".format(options.range_from, options.range_to))
            file.write("Execution time: {}s\n\n".format(execution_time))

            file.write("Epochs: {}\n".format(options.epochs_amount))
            file.write("Population size: {}\n".format(options.population_size))
            file.write("Precision: {}\n".format(options.precision))
            file.write("Elite strategy amount: {}\n".format(options.elite_strategy_amount))
            file.write("Selection: {}, param: {}\n".format(options.selection_method, options.selection_param))
            file.write("Crossover: {}, probability: {}\n".format(options.crossover_method, options.crossover_probability))
            file.write("Mutation: {}, probability: {}\n".format(options.mutation_method, options.mutation_probability))
            file.write("Inversion probability: {}\n".format(options.inversion_probability))
