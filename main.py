from population import Population

def main():
    # Konfiguracja parametrów algorytmu genetycznego
    population_size = 20  # Rozmiar populacji
    chromosome_length = 1  # Długość chromosomu
    lower_bound = -10.0  # Dolna granica wartości zmiennej
    upper_bound = 10.0  # Górna granica wartości zmiennej
    generations = 1  # Liczba generacji
    crossover_rate = 0.8  # Współczynnik krzyżowania
    mutation_rate = 0.05  # Współczynnik mutacji
    inversion_rate = 0.2  # Prawdopodobieństwo inwersji
    elitism_rate = 0.10  # Współczynnik elitarności
    selection_type = "best"  # Metoda selekcji
    crossover_type = "one_point"  # Typ krzyżowania
    mutation_type = "two_point"  # Typ mutacji
    bit_length = 25  # Liczba bitów na zmienną
    value_range = (-10, 10)  # Zakres wartości zmiennych
    mode = "minimize"  # Tryb działania algorytmu (minimalizacja lub maksymalizacja)

    # Tworzenie populacji początkowej
    population = Population(population_size, chromosome_length, lower_bound, upper_bound, bit_length, value_range)

    # Ewolucja populacji
    for generation in range(generations):
        # Ocena przystosowania populacji
        population.evaluate_fitness(mode)
        # Wyświetlanie najlepszej wartości przystosowania w danej generacji
        print(f"Generacja {generation} - najlepsze przystosowanie: {min([ind.fitness for ind in population.individuals]) if mode == 'minimize' else max([ind.fitness for ind in population.individuals])}")
        # Generowanie kolejnej populacji
        population.generate_next_population(mutation_rate, mutation_type, crossover_type, elitism_rate, inversion_rate, selection_type)

if __name__ == "__main__":
    main()