class mergesort:
    @staticmethod
    def __merge(array, array1, array2):
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


    @staticmethod
    def __sort(array):
        length = len(array)

        if length == 1:
            return array

        mid = length//2
        array1 = array[:mid]
        array2 = array[mid:]

        mergesort.__sort(array1)
        mergesort.__sort(array2)
        mergesort.__merge(array, array1, array2)


    def __init__(self, array):
        mergesort.__sort(array)
