from time import perf_counter_ns
from random import randint


def insertionsort(array):
    length = len(array)

    for index in range(1, length):
        value = array[index]
        if value > array[index-1]:
            continue

        array.pop(index)

        for index2 in range(index, -1, -1):
            if value >= array[index2-1]:
                break
            
        array.insert(index2, value)


        
if __name__ == "__main__":

    n = 10
    trials = 10**7
    
    total_time = 0
    total_time_squared = 0

    for _ in range(trials):
        array = [randint(1, n) for _ in range(n)]

        start_time = perf_counter_ns()
        insertionsort(array)
        end_time = perf_counter_ns()

        time = end_time - start_time
        total_time += time
        total_time_squared += time**2
    
    mean_time = total_time/trials
    standard_deviation = ((total_time_squared - trials * mean_time**2)/(trials - 1))**0.5
    
    print(f"mean = {round(mean_time)} ns")
    print(f"standard deviation = {round(standard_deviation)} ns")