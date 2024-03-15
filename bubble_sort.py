def bubble_sort(list):
    list_length = len(list)
    for i in range(list_length):
        # iterate through the list and swap two elements
        # if firts is greater than second
        for j in range(list_length - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list
