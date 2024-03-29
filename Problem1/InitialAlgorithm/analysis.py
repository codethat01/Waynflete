from math import gcd
from sympy import perfect_power
from time import perf_counter_ns


def solve_equation(n):
    solutions = [(1, 1, 1, 1)]

    for m in range(2, n-1):
        if m % (n-m) == 0:
            x = m//(n-m)
            solutions.append((m, x, m, x+1))

        else:
            hcf = gcd(m, n-m)
            y = (n-m)//hcf
            ret = perfect_power(m, [y])

            if ret:
                x = m//hcf
                z = ret[0]
                solutions.append((z, x, z, x+y))

    if n != 2:
        solutions.append((n-1, n-1, n-1, n))
    
    return solutions

      
    
if __name__ == "__main__":

    n = 10
    trials = 10**7
    
    total_time = 0
    total_time_squared = 0

    for t in range(trials):
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