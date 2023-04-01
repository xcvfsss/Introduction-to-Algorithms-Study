def quick_sort_iterative(arr):
    if len(arr) <= 1:
        return arr
    def partition(low, high):
        pivot = arr[low]
        i = low + 1
        j = high
        while True:
            # 小于或者等于轴的元素移动到左边
            while i <= j and arr[i] <= pivot:
                i += 1
            # 大于轴的元素移动到右边
            while i <= j and arr[j] > pivot:
                j -= 1
            # 如果两个while结束后i小于或等于j，则arr[i]是找到到第一个大于轴的元素，arr[j]是
            # 第一个小于轴的元素，于是交换这两个元素，多次循环后，大于轴的元素在左边，小于轴的元素
            # 在右边
            if i <= j:
                arr[j], arr[i] = arr[i], arr[j]
            else:
                break
        # 最终将轴所指向的元素与j所指向的元素交换，之所以是j，因为结束循环后i>j,且i-j=1，此时i左边
        # 的元素都小于pivot，j右边的元素都大于pivot，j在i的左边一格，所以arr[j]<arr[i]，由于我
        # 选择的pivot是arr[0]，处于左边位置，所以应该将pivot和arr[j]的值互换
        arr[low], arr[j] = arr[j], arr[low]
        return j
    stack =[(0, len(arr)-1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(low, high)
            stack.extend([(low, pivot_index - 1),(pivot_index + 1, high)])
    return arr

my_list = [3, 6, 5, 3, 6, 8, 2, 5, 89, 54, 63, 12, 76, 98, 34, 56, 78, 4, 23, 15, 16, 8, 10, 1, 2, 1]
print(quick_sort_iterative(my_list))