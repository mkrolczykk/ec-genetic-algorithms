def apply_elitism(individuals, elitism_rate):
    # Funkcja apply_elitism wybiera najlepszych osobników, którzy przechodzą bez zmian do kolejnej generacji
    sorted_individuals = sorted(individuals, key=lambda ind: ind.fitness)
    elite_count = int(len(individuals) * elitism_rate)
    return sorted_individuals[:elite_count]
