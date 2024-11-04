import tkinter as tk
from tkinter import ttk
from apoor import fdir

from logic.crossover.crossover_factory import CrossoverMethod
from logic.functions.functions_factory import FitnessFunction
from logic.mutation.mutation_factory import MutationMethod
from logic.selection.selection_factory import SelectionMethod
from ui.components.select_box import SelectBox


class View(ttk.Frame):
    GRID_GAP_X = 16
    GRID_GAP_Y = 8

    def __init__(self, parent):
        super().__init__(parent, padding=16)

        number_of_columns = 3

        for column_index in range(number_of_columns):
            self.columnconfigure(column_index, weight=1)

        self.fitness_function = self.add_selectbox(
            FitnessFunction.EGGHOLDER_FUNCTION,
            fdir(FitnessFunction),
            "FitnessFunction",
            0, 0)

        self.number_of_variables = self.add_spinbox(2, "Number of variables", 2, 20, 0, 1)
        self.range_from = self.add_spinbox(-10, "Range from", -100, 100, 0, 2)
        self.range_to = self.add_spinbox(10, "Range to", -100, 100, 0, 3)
        self.population_size = self.add_spinbox(40, "Population size", 0, 100, 0, 4)
        self.epochs_amount = self.add_spinbox(100, "Epochs amount", 0, 100, 0, 5)

        self.selection_method = self.add_selectbox(
            SelectionMethod.BEST,
            fdir(SelectionMethod),
            "Selection method",
            1, 0)

        self.crossover_method = self.add_selectbox(
            CrossoverMethod.ONE_POINT,
            fdir(CrossoverMethod),
            "Crossover method",
            1, 1)

        self.mutation_method = self.add_selectbox(
            MutationMethod.ONE_POINT,
            fdir(MutationMethod),
            "Mutation method",
            1, 2)

        self.grain_size = self.add_spinbox(2, "Grain Size (crossover granular)", 2, 10, 1, 3)
        self.elite_strategy_amount = self.add_spinbox(1, "Elite Strategy amount", 0, 100, 1, 4)
        self.precision = self.add_spinbox(5, "Precision", 0, 20, 1, 5)

        self.selection_param = self.add_spinbox(60, "Selection param ([%] - BEST, k)", 0, 100, 2, 0)
        self.crossover_probability = self.add_spinbox(70, "Crossover probability [%]", 0, 100, 2, 1)
        self.mutation_probability = self.add_spinbox(20, "Mutation probability [%]", 0, 100, 2, 2)
        self.inversion_probability = self.add_spinbox(20, "Inversion probability [%]", 0, 100, 2, 3)

        self.maximization = tk.StringVar()
        checkbox = ttk.Checkbutton(
            self,
            text="Maximization",
            variable=self.maximization,
            onvalue="1",
            offvalue="")
        checkbox.grid(column=2, row=4, sticky=tk.SW, padx=self.GRID_GAP_X, pady=self.GRID_GAP_Y)

        button = ttk.Button(
            self,
            text="Start",
            style="Accent.TButton",
            command=self.submit)
        button.grid(column=2, row=4, sticky=tk.SE, padx=self.GRID_GAP_X, pady=self.GRID_GAP_Y)

        self.controller = None

    def submit(self):
        self.controller.submit(
            self.fitness_function.get(),
            int(self.number_of_variables.get()),
            float(self.range_from.get()),
            float(self.range_to.get()),
            int(self.population_size.get()),
            int(self.precision.get()),
            int(self.epochs_amount.get()),
            int(self.grain_size.get()),
            int(self.elite_strategy_amount.get()),
            int(self.crossover_probability.get()),
            int(self.mutation_probability.get()),
            int(self.inversion_probability.get()),
            self.selection_method.get(),
            int(self.selection_param.get()),
            self.crossover_method.get(),
            self.mutation_method.get(),
            bool(self.maximization.get()))

    def set_controller(self, controller):
        self.controller = controller

    def add_spinbox(self, value, text, from_, to, column, row):
        variable = tk.StringVar(value=value)
        frame = ttk.Frame(self)
        label = ttk.Label(frame, text=text)
        input_ = ttk.Spinbox(frame, from_=from_, to=to, textvariable=variable)

        self.set_component(frame, label, input_, column, row)
        return variable

    def add_selectbox(self, value, possible_values, text, column, row):
        variable = tk.StringVar(value=value)
        frame = ttk.Frame(self)
        label = ttk.Label(frame, text=text)
        input_ = SelectBox(frame, variable, values=possible_values)

        self.set_component(frame, label, input_, column, row)
        return variable

    def set_component(self, frame, label, input_, column, row):
        label.pack(fill=tk.X)
        input_.pack(fill=tk.X, pady=(4, 0))
        frame.grid(column=column, row=row, sticky=tk.EW, padx=self.GRID_GAP_X, pady=self.GRID_GAP_Y)