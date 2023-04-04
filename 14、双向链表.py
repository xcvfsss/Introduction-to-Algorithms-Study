class ListNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, value):
        new_node = ListNode(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert(self, position, value):
        if position <= 0:
            # 返回的是个什么东西，待会问一下chatgpt
            return self.prepend(value)
        elif position >= self.size():
            return self.append(value)

        new_node = ListNode(value)
        current = self.head
        for _ in range(position - 1):
            current = current.next
        new_node.prev = current
        new_node.next = current.next
        current.next.prev = new_node
        current.next = new_node

    def prepend(self, value):
        new_node = ListNode(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def remove(self, value):
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return ' <-> '.join(str(x) for x in values)


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    print(dll)  # 1 <-> 2 <-> 3
    dll.prepend(0)
    print(dll)  # 0 <-> 1 <-> 2 <-> 3
    dll.insert(2, 1.5)
    print(dll)  # 0 <-> 1 <-> 1.5 <-> 2 <-> 3
    dll.remove(1.5)
    print(dll)  # 0 <-> 1 <-> 2 <-> 3
