from sympy import perfect_power, divisors as get_divisors
from math import log2, gcd
from random import randint
from time import perf_counter_ns


def solve_equation(n):
    solutions = [(1, 1, 1, 1)]

    if n == 2:
        return solutions

    divisors = get_divisors(n)
    divisors.pop()

    for d in divisors:
        x = n//d

        solutions.append((n-d, x-1, n-d, x))

        for y in range(2, min(int(log2(n)) + 1, x)):
            if gcd(x, y) == 1:
                ret = perfect_power(n - y*d, [y])

                if ret:
                    z = ret[0]
                    solutions.append((z, x - y, z, x))
    
    return solutions

        
    
if __name__ == "__main__":

    nmin, nmax = 2, 10
    trials = 10**7
    
    total_time = 0
    total_time_squared = 0

    for t in range(trials):
        n = randint(nmin, nmax)
        start_time = perf_counter_ns()
        solve_equation(n)
        end_time = perf_counter_ns()

        time = end_time - start_time
        total_time += time
        total_time_squared += time**2

    mean_time = total_time/trials
    standard_deviation = ((total_time_squared - trials * mean_time**2)/(trials - 1))**0.5
    
    print(f"mean = {round(mean_time)} ns")
    print(f"standard deviation = {round(standard_deviation)} ns")