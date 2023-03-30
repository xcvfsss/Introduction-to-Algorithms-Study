def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    '''
                    0
            1               2
        3       4       5       6 
        如果左孩子节点是i，则父亲节点是 (i+1)/2 -1
        如果右孩子节点是i，则父亲节点是 (i+1)//2 -1
        所以，如果子节点是i，则父亲节点是 (i+1)//2 -1
        所以数组长度为n的堆，最后一个节点的索引是n-1，那么他的父节点是 n//2 -1
    '''
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # 构建最大堆
    # 从最后一个子节点的父节点开始遍历，一直遍历到数组的最后一个节点arr[0]
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 从一个堆顶抽取元素，放到数组的末尾，然后重新调整堆
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    heap_sort(arr)
    print("Sorted array is:", arr)