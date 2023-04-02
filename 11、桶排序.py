def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        up = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > up:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = up
    return bucket


def bucket_sort(arr):
    if not arr:
        return []

    max_val, min_val = max(arr), min(arr)
    bucket_count = len(arr)
    bucket_range = (max_val - min_val) / bucket_count

    # 初始化桶
    buckets = [[] for _ in range(bucket_count + 1)]

    # 将元素分配到对应的桶中
    for num in arr:
        index = int((num - min_val) // bucket_range)
        buckets[index].append(num)

    # 对每个桶进行插入排序
    sorted_arr = []
    for bucket in buckets:
        if bucket:
            sorted_arr.extend(insertion_sort(bucket))

    return sorted_arr


my_list = [3, 6, 8, 10, 1, 2, 1]
print(bucket_sort(my_list))
