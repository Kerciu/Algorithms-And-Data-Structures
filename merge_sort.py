def merge_sort(list):
    if len(list) <= 1:
        return list
    middle_point = len(list) // 2
    left_part = list[:middle_point]
    right_part = list[middle_point:]
    sorted_left_part = merge_sort(left_part)
    sorted_right_part = merge_sort(right_part)
    return merge_lists(sorted_left_part, sorted_right_part)


def merge_lists(left_part, right_part):
    left_index = 0
    right_index = 0
    merged_list = []
    while (left_index < len(left_part) and right_index < len(right_part)):
        if left_part[left_index] > right_part[right_index]:
            merged_list.append(right_part[right_index])
            right_index += 1
        else:
            merged_list.append(left_part[left_index])
            left_index += 1
    if left_index < len(left_part):
        merged_list.extend(left_part[left_index:])
    elif right_index < len(right_part):
        merged_list.extend(right_part[right_index:])
    return merged_list
