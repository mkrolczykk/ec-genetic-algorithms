import math

def griewank_function(x):
    # Funkcja celu Griewanka oblicza wartość funkcji Griewanka dla danego wektora x
    sum_part = sum([(xi ** 2) / 4000 for xi in x])
    product_part = math.prod([math.cos(xi / math.sqrt(i + 1)) for i, xi in enumerate(x)])
    return sum_part - product_part + 1

