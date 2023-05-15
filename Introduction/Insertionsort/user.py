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

    array = list(map(int, input().split()))
    insertionsort(array)
    print(*array)