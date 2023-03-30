
# 根节点的索引index是1
class PriorityQueue:

    def __init__(self):
        self._queue = [None]  # 第一个元素设为 None 以简化索引计算

    def _parent(self, index):
        return index // 2

    def _left_child(self, index):
        return index * 2

    def _right_child(self, index):
        return index * 2 + 1

    def _swap(self, index1, index2):
        self._queue[index1], self._queue[index2] = self._queue[index2], self._queue[index1]

    def _sift_up(self, index):
        while index > 1 and self._queue[self._parent(index)][1] < self._queue[index][1]:
            self._swap(index, self._parent(index))
            index = self._parent(index)

    def _sift_down(self, index):
        max_index = index
        left_child = self._left_child(index)
        right_child = self._right_child(index)

        if left_child < len(self._queue) and self._queue[left_child][1] > self._queue[max_index][1]:
            max_index = left_child

        if right_child < len(self._queue) and self._queue[right_child][1] > self._queue[max_index][1]:
            max_index = right_child

        if index != max_index:
            self._swap(index, max_index)
            self._sift_down(max_index)

    def push(self, item, priority):
        self._queue.append((item, priority))
        self._sift_up(len(self._queue) - 1)

    def pop(self):
        if len(self._queue) <= 1:
            raise IndexError("队列为空，无法弹出元素。")

        max_item = self._queue[1][0]
        self._queue[1] = self._queue[-1]
        self._queue.pop()
        self._sift_down(1)

        return max_item

    def is_empty(self):
        return len(self._queue) == 1

# 示例：
pq = PriorityQueue()
pq.push("任务1", 1)
pq.push("任务2", 3)
pq.push("任务3", 2)

print(pq.pop())  # 输出: 任务2
print(pq.pop())  # 输出: 任务3
print(pq.pop())  # 输出: 任务1
