def max_subarray(my_array):
    if len(my_array) == 1:
        return my_array[0], my_array
    mid = len(my_array) // 2
    left_max_size, left_max_array = max_subarray(my_array[:mid])
    right_max_size, right_max_array = max_subarray(my_array[mid:])
    mid_cross_size, mid_corss_array = max_cross_subarray(my_array, mid)

    max_sum=max(left_max_size,right_max_size,mid_cross_size)

    if max_sum == left_max_size:
        return left_max_size, left_max_array
    elif max_sum == right_max_size:
        return right_max_size, right_max_array
    else:
        return mid_cross_size, mid_corss_array



def max_cross_subarray(my_array,mid):
    left_max = float('-inf')
    left_sum = 0
    left_index = 0
    for i in range(mid-1, -1, -1):
        left_sum += my_array[i]
        if left_sum > left_max:
            left_max = left_sum
            left_index = i
    right_max = float('-inf')
    right_sum = 0
    right_index =0
    for i in range(mid, len(my_array), 1):
        right_sum += my_array[i]
        if right_sum > right_max:
            right_max = right_sum
            right_index = i + 1
    return left_max + right_max, my_array[left_index : right_index]

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, max_sum_subarray = max_subarray(nums)
print(max_sum, max_sum_subarray)

