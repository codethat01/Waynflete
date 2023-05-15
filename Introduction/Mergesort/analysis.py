from time import perf_counter_ns
from random import randint


def mergesort(array):
    length = len(array)

    if length == 1:
        return array

    mid = length//2
    array1 = array[:mid]
    array2 = array[mid:]

    mergesort(array1)
    mergesort(array2)
    
    index, index1, index2 = 0, 0, 0
    length = len(array)

    maximum = max(array1[-1], array2[-1]) + 1
    array1.append(maximum)
    array2.append(maximum)

    while index < length:
        v1, v2 = array1[index1], array2[index2]

        if v1 < v2:
            array[index] = v1
            index1 += 1
        else:
            array[index] = v2
            index2 += 1

        index += 1


        
if __name__ == "__main__":

    n = 10
    trials = 10**7
    
    total_time = 0
    total_time_squared = 0

    for _ in range(trials):
        array = [randint(1, n) for _ in range(n)]

        start_time = perf_counter_ns()
        mergesort(array)
        end_time = perf_counter_ns()

        time = end_time - start_time
        total_time += time
        total_time_squared += time**2
    
    mean_time = total_time/trials
    standard_deviation = ((total_time_squared - trials * mean_time**2)/(trials - 1))**0.5
    
    print(f"mean = {round(mean_time)} ns")
    print(f"standard deviation = {round(standard_deviation)} ns")