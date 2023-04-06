from math import comb as binomial_coefficient
from time import perf_counter_ns


def calculate_coefficient(n, k, coefficients):
    total = binomial_coefficient(n, k) * ((-1) ** k)

    for m in range(n):
        intermediate_sum = 0

        for r in range(min(k, m+1)):
            intermediate_sum += coefficients[m][r] * binomial_coefficient(n-m-1, k-r-1) * ((-1) ** (k-r-1))

        total += binomial_coefficient(n, m) * intermediate_sum
    
    return total


def generate_coefficients(max_n):
    coefficients = [[1]+[0]*length for length in range(max_n+1)]

    for n in range(1, max_n+1):
        for k in range(1, n):
            coefficients[n][k] = calculate_coefficient(n, k, coefficients)
    
    return coefficients

        
    
if __name__ == "__main__":

    n = 100
    trials = 10**3
    
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
