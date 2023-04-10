from math import comb as binomial_coefficient
from time import perf_counter_ns


def calculate_coefficient(n, k):
    total = 0

    for j in range(k+1):
        total += binomial_coefficient(n+1, j) * ((k - j + 1) ** n) * ((-1) ** j)

    return total


def generate_coefficients(n):
    if n == 0:
        return [1]
    
    coefficients = [0]*n

    for k in range(n):
        coefficients[k] = calculate_coefficient(n, k)
    
    return coefficients

        
    
if __name__ == "__main__":

    n = 100
    trials = 10**2
    
    total_time = 0
    total_time_squared = 0

    for t in range(trials):
        start_time = perf_counter_ns()
        generate_coefficients(n)
        end_time = perf_counter_ns()

        time = end_time - start_time
        total_time += time
        total_time_squared += time**2

    mean_time = total_time/trials
    standard_deviation = ((total_time_squared - trials * mean_time**2)/(trials - 1))**0.5
    
    print(f"mean = {round(mean_time)} ns")
    print(f"standard deviation = {round(standard_deviation)} ns")
