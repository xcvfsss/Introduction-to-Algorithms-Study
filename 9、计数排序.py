def counting_sort(arr):
    if not arr:
        return []

    min_value = min(arr)
    max_value = max(arr)
    count_array = [0] * (max_value - min_value + 1)

    for value in arr:
        count_array[value - min_value] += 1

    sorted_arr = []
    for index, count in enumerate(count_array):
        sorted_arr.extend([index + min_value] * count)

    return sorted_arr


my_list = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(my_list))