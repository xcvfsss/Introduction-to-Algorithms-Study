
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    sorted_arr = [0] * n
    count = [0] * 10
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1,10):
        count[i] += count[i-1]
    i = n -1
    while i >= 0 :
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

my_list = [179, 48, 77, 96, 805, 24, 3, 62,71,90,89,28,48,48,431]
print(radix_sort(my_list))



