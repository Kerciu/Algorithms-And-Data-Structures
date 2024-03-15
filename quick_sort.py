def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    # Determine pivot
    pivot = arr[len(arr) // 2]

    less = []
    equal = []
    greater = []

    # Divide arr into 3 lists based on pivot
    for elem in arr:
        if elem < pivot:
            less.append(elem)
        elif elem == pivot:
            equal.append(elem)
        else:
            greater.append(elem)

    # Sort recursively lesser and greater elements
    return quick_sort(less) + equal + quick_sort(greater)
