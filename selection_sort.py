def selection_sort(arr: list) -> list:
    for i in range(len(arr)):
        # capture current character
        for j in range(i + 1, len(arr)):

            # iterate through the list above the captured character to the end
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr
