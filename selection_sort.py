def selection_sort(list):
    for i in range(len(list)):
        # capture current character
        for j in range(i + 1, len(list)):
            # iterate through the list above the captured character to the end
            if list[j] < list[i]:
                list[i], list[j] = list[j], list[i]
    return list
