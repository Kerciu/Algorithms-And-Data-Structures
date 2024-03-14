def selection_sort(arr):

    for i in range(len(arr)):
        minimumIndex = i

        for j in range(i + 1, len(arr)):

            if arr[j] < arr[minimumIndex]:
                minimumIndex = j
    
        (arr[i], arr[minimumIndex]) = (arr[minimumIndex], arr[i])

    return arr
