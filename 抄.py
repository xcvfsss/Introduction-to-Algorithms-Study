
class PriorityQueue:
    def __init__(self):
        self._queue = [None]

    def _parent(self, index):
        return index // 2

    def _left_child(self, index):
        return index * 2

    def _right_child(self, index):
        return index * 2 + 1

    def _swap(self, index1, index2):
        self._queue[index1], self._queue[index2] = self._queue[index2], self._queue[index1]

    def _sift_up(self, index):
        while index > 1 and self._queue[index //2][1] < self._queue[index][1]:
            self._swap(index, index // 2)
            index = index // 2

    def _sift_dowm(self, index):
        max_index = index
        left_child = self._left_child(index)
        right_child = self._right_child(index)

        if left_child < len(self._queue) and self._queue[left_child][1] > self._queue[max_index][1]:
            max_index = left_child
        if right_child < len(self._queue) and self._queue[right_child][1] > self._queue[max_index][1]:
            max_index = right_child
        if max_index != index:
            self._swap(index, max_index)
            self._sift_dowm(max_index)

    def push(self, item, priority):
        self._queue.append((item, priority))
        self._sift_up(len(self._queue) - 1)

    def pop(self):
        if len(self._queue) <= 1:
            raise IndexError('队列为空，无法弹出元素')
        max_item = self._queue[1][0]
        self._queue[1] = self._queue[-1]
        self._queue.pop()
        self._sift_dowm(1)
        return max_item

    def is_empty(self):
        return len(self._queue) == 1

pq = PriorityQueue()
pq.push("任务1", 1)
pq.push("任务2", 3)
pq.push("任务3", 45)
pq.push("任务4", 62)
pq.push("任务5", 50)
pq.push("任务6", 16)
pq.push("任务7", 42)
pq.push("任务8", 58)
pq.push("任务9", 92)
pq.push("任务10", 12)
pq.push("任务11", 5)
pq.push("任务12", 8)
pq.push("任务13", 9)
pq.push("任务14", 6)

print(pq._queue)
print(pq.pop())  # 输出: 任务2
print(pq.pop())  # 输出: 任务3
print(pq.pop())  # 输出: 任务1














