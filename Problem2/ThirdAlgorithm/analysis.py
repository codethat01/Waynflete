from time import perf_counter_ns


def update_coefficient(n, k, coefficients):
    coefficients[k] *= k+1
    coefficients[k] += (n-k) * coefficients[k-1] 
  

def generate_coefficients(max_n):
    coefficients = [1] + [0]*(max_n-1)

    for n in range(1, max_n+1):
        for k in range(n-1, 0, -1):
            update_coefficient(n, k, coefficients)
    
    return coefficients

        
    
if __name__ == "__main__":

    n = 20
    trials = 10**6
    
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
    print(f"{round(mean_time):,} ± {round(standard_deviation):,}") # delete me