def max_subarray(nums):
    max_sum = float('-inf')
    current_sum = 0
    start_index = 0
    end_index = 0
    temp_start_index = 0

    for i, num in enumerate(nums):
        if current_sum <= 0:
            current_sum = num
            temp_start_index = i
        else:
            current_sum += num

        if current_sum > max_sum:
            max_sum = current_sum
            start_index = temp_start_index
            end_index = i

    return max_sum, nums[start_index:end_index + 1]

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, max_sum_subarray = max_subarray(nums)
print(max_sum, max_sum_subarray)