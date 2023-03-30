def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left_sort = merge_sort(left)
    right_sort = merge_sort(right)
    return merge(left_sort, right_sort)

def merge(left, right):
    result = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] >= right[r]:
            result.append(right[r])
            r += 1
        else:
            result.append(left[l])
            l += 1
    if l == len(left):
        while r < len(right):
            result.append(right[r])
            r += 1
    if r == len(right):
        while l < len(left):
            result.append(left[l])
            l += 1
    return result

arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)





