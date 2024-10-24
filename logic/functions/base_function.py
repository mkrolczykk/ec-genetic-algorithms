class BaseFunction:

    def calculate_fitness(self, real_values):
        raise NotImplementedError("Dodaj metode calculate_fitness")

    def fitness(self, real_values):
        return self.calculate_fitness(real_values)

