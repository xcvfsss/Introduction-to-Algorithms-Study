# arr是待排序的数组，exponent用于确定排序依据的次数，例如个位数十位数百位数等等
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    # sorted_arr用于存放排序后的结果
    sorted_arr = [0] * n
    # count用于存储0-9的每个数字出现次数
    count = [0] * 10

    # 构建计数数组count，例如：count = [0, 1, 2, 2, 1, 0, 0, 0, 1, 0]
    # （数字 1 有 1 个，数字 2 有 2 个，数字 3 有 2 个，数字 4 有 1 个，数字 8 有 1 个）
    for i in range(n):
        # 用于计算当前元素的指定位数的值
        index = arr[i] // exp
        # 当arr[i]的值是135，而exp是10，index的值是13，此时要取出3这个数
        count[index % 10] += 1


    #  通过构建累计计数数组，我们可以知道小于等于当前值的元素个数，从而推断出
    #  当前值在输出排序数组中的位置。
    #  count = [0, 1, 3, 5, 6, 6, 6, 6, 7, 7]
    # （小于等于 1 的有 1 个，小于等于 2 的有 3 个，小于等于 3 的有 5 个，依此类推）
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 初始化索引变量 i，从输入数组的最后一个元素开始。
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        sorted_arr[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = sorted_arr[i]

def radix_sort(arr):
    if not arr:
        return []

    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

    return arr

my_list = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(my_list))
