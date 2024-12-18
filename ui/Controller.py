class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def submit(self,
               fitness_function,
               number_of_variables,
               range_from,
               range_to,
               population_size,
               precision,
               epochs_amount,
               grain_size,
               elite_strategy_amount,
               crossover_probability,
               crossover_alpha,
               crossover_beta,
               mutation_probability,
               inversion_probability,
               selection_method,
               selection_param,
               crossover_method,
               mutation_method,
               maximization):
        self.model.fitness_function = fitness_function
        self.model.number_of_variables = number_of_variables
        self.model.range_from = range_from
        self.model.range_to = range_to
        self.model.population_size = population_size
        self.model.precision = precision
        self.model.epochs_amount = epochs_amount
        self.model.grain_size = grain_size
        self.model.elite_strategy_amount = elite_strategy_amount
        self.model.crossover_probability = crossover_probability
        self.model.crossover_alpha = crossover_alpha
        self.model.crossover_beta = crossover_beta
        self.model.mutation_probability = mutation_probability
        self.model.inversion_probability = inversion_probability
        self.model.selection_method = selection_method
        self.model.selection_param = selection_param
        self.model.crossover_method = crossover_method
        self.model.mutation_method = mutation_method
        self.model.maximization = maximization

        self.model.run_algorithm()
