def bubblesort(array):
    swapped = True
    while swapped:
        swapped = False
        for index in range(len(array)-1):
            if array[index] > array[index+1]:
                array[index], array[index+1] = array[index+1], array[index]
                swapped = True
