def merge_sort(list):
    list_length = len(list)

    if list_length <= 1:
        return list

    # count the middle element of the list,round down
    middle_point = list_length // 2

    # seperate list to two halfs
    left_part = list[:middle_point]
    right_part = list[middle_point:]

    # sort seperated list parts
    sorted_left_part = merge_sort(left_part)
    sorted_right_part = merge_sort(right_part)

    # merge seperated lists
    return merge_lists(sorted_left_part, sorted_right_part)


def merge_lists(left_part, right_part):
    # point next unmerged element from each list
    left_part_length = len(left_part)
    right_part_length = len(right_part)
    left_index = 0
    right_index = 0

    merged_list = []
    # add next elements from lists to merged_list in correct order
    while (left_index < left_part_length and right_index < right_part_length):
        if left_part[left_index] > right_part[right_index]:
            merged_list.append(right_part[right_index])
            right_index += 1
        else:
            merged_list.append(left_part[left_index])
            left_index += 1

    # add rest of elements which were not added in the loop
    if left_index < left_part_length:
        merged_list.extend(left_part[left_index:])
    elif right_index < right_part_length:
        merged_list.extend(right_part[right_index:])

    return merged_list
