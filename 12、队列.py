class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty")

    def size(self):
        return len(self.queue)

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty")

# 测试
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.front())  # 输出：1
print(q.dequeue())  # 输出：1
print(q.front())  # 输出：2
print(q.size())  # 输出：2
