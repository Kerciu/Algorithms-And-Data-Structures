def bubble_sort(arr: list) -> list:
    arr = arr.copy()
    # Bubble sort algorithm

    for i in range(len(arr)):

        # second index to not go above array length limit
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:

                # Initialize temporary variables to store arr[i]
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr
