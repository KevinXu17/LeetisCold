# Always pick the first element as a pivot
# Always pick the last element as a pivot
# Pick a random element as a pivot
# Pick median as a pivot

# TODO pointer is the future index of pivot
#   pointer                                   pivot
#   (i)-1    0      1      2      3      4      5
#            3      2      1      7      8      5

def partition(array, low, high):
    #TODO set pivot
    pivot = array[high]
    #TODO i is the position of pivot
    i = low - 1
    for j in range(low, high):  #TODO between 0 to before pivot (high-1)
        if array[j] <= pivot:
            #TODO found less or equal to pivot, i moves up
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    #TODO move pivot to i
    (array[i+1], array[high]) = (array[high], array[i+1])

    return i + 1

def quickSort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quickSort(array, low, pivot - 1)
        quickSort(array, pivot + 1, high)


examples = [8, 4, 1, 5, 5, 2, 9, 5]
quickSort(examples, 0, len(examples) - 1)
print(examples)