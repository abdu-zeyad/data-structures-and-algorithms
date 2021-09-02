def insertionSort(arr):

    for i in range(1, len(arr)):

        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


arr = [8, 4, 23, 42, 16, 15]
soreted_arr = insertionSort(arr)
print(soreted_arr)
