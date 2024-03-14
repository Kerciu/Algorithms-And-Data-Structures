def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = len(lst) // 2
    left = lst[:middle]
    right = lst[middle:]
    sleft = merge_sort(left)
    sright = merge_sort(right)
    return merge(sleft, sright)


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while (left_index < len(left) and right_index < len(right)):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result
