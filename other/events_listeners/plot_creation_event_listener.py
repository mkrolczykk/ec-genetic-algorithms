import pathlib
import matplotlib
from matplotlib import pyplot as plt
from pubsub import pub
from other.events.event_algorithm_completed import EventAlgorithmCompleted
from other.events_listeners.event_listener import EventListener

matplotlib.use("SVG")


class PlotCreationEventListener(EventListener):
    def listen(self):
        pub.subscribe(self.__handle, EventAlgorithmCompleted.__name__)

    @staticmethod
    def __handle(event: EventAlgorithmCompleted):
        epochs = []
        best = []
        average = []
        std = []

        for epoch, generation in enumerate(event.generations):
            best_candidate = generation.get_best_candidate(maximization=event.options.maximization)
            epochs.append(epoch)
            best.append(best_candidate.score)
            average.append(generation.get_average_score())
            std.append(generation.get_standard_deviation())

        dir_path = "output/" + event.time_finished
        pathlib.Path(dir_path).mkdir(parents=True, exist_ok=True)

        PlotCreationEventListener.__create_best_plot(epochs, best, dir_path + "/best.png")
        PlotCreationEventListener.__create_average_plot(epochs, average, std, dir_path + "/average.png")

    @staticmethod
    def __create_best_plot(epochs, bests, file_name):
        fig = plt.figure(figsize=(14, 8))

        plt.xlabel("epoch")
        plt.ylabel("best score")
        plt.title("Best score in each epoch")

        plt.plot(epochs, bests)

        plt.savefig(file_name)
        plt.close(fig)

    @staticmethod
    def __create_average_plot(epochs, averages, stds, file_name):
        fig = plt.figure(figsize=(14, 8))

        plt.xlabel("epoch")
        plt.ylabel("average score")
        plt.title("Average score with standard deviation in each epoch")

        plt.errorbar(epochs, averages, yerr=stds, ecolor='r', elinewidth=0.7, linewidth=1, capsize=1)

        plt.savefig(file_name)
        plt.close(fig)
