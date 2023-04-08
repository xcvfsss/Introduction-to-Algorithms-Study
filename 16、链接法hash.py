class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    def __iter__(self):
        current = self.head
        while current:
            yield current.key, current.value
            current = current.next

    def is_contains(self, key):
        current = self.head
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

    def __setitem__(self, key, value):
        current = self.head
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next
        raise KeyError('Key not found')

    def append(self, key, value):
        new_node = Node(key, value)
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
        else:
            self.head = new_node
        self.tail = new_node

    def find(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return None

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [LinkedList() for _ in range(self.size)]
        self.load_factor = 0.6
        self.max_length = 10
        self.num_elements = 0

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __delitem__(self, key):
        self.delete(key)

    def __contains__(self, key):
        index = self._hash(key)
        linked_list = self.table[index]
        return linked_list.is_contains(key)

    def __len__(self):
        return self.num_elements

    def __iter__(self):
        for linked_list in self.table:
            current = linked_list.head
            while current:
                yield current.key
                current = current.next

    def _hash(self, key):
        return hash(key) % self.size

    def _rehash(self, old_hash, step):
        return (old_hash + step) % self.size

    def _resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [LinkedList() for _ in range(self.size)]
        self.num_elements = 0

        for linked_list in old_table:
            current = linked_list.head
            while current:
                self.put(current.key, current.value)
                current = current.next

    def put(self, key, value):
        # 检查当前哈希表的元素数量与表的大小之比是否大于预设的负载因子。如果是，则说明需要对哈希表进行扩容。
        if self.num_elements / self.size > self.load_factor:
            # 对哈希表进行扩容。这个操作将哈希表的大小翻倍，重新分配所有元素到新的哈希槽中。
            self._resize()
        # 计算键值 key 的哈希值，并找到对应的哈希槽索引。
        index = self._hash(key)
        # 获取当前索引对应的哈希槽的链表
        linked_list = self.table[index]

        # 判断当前链表是否已经包含了给定的键值 key。如果包含，则更新对应的值。
        if linked_list.is_contains(key):
            # 如果链表已经包含了给定的键值 key，则更新对应的值。
            linked_list[key] = value
        # 如果链表不包含给定的键值 key，则执行以下操作。
        else:
            # 判断当前链表的长度是否小于预设的最大长度。如果是，则在当前链表中添加新的键值对。
            if len(linked_list) < self.max_length:
                # 在当前链表中添加新的键值对。
                linked_list.append(key, value)
                # 更新哈希表中的元素数量。
                self.num_elements += 1
            # 如果当前链表的长度大于等于预设的最大长度，则需要在其他哈希槽中找到合适的位置来存储新的键值对或者更新键值对。
            else:
                # 通过再哈希找到下一个可能的哈希槽。
                next_slot = self._rehash(index, 1)
                # 使用无限循环来遍历哈希槽，直到找到合适的位置来存储新的键值对或者更新键值对。
                while True:
                    # 获取下一个哈希槽的链表。
                    next_linked_list = self.table[next_slot]
                    # 判断下一个链表是否已经包含了给定的键值 key。如果包含，则更新对应的值。
                    if next_linked_list.is_contains(key):
                        # 如果下一个链表已经包含了给定的键值 key，则更新对应的值。
                        next_linked_list[key] = value
                        break
                    # 判断下一个链表的长度是否小于预设的最大长度。如果是，则在下一个链表中添加新的键值对。
                    elif len(next_linked_list) < self.max_length:
                        # 在下一个链表中添加新的键值对。
                        next_linked_list.append(key, value)
                        # 更新哈希表中的元素数量。
                        self.num_elements += 1
                        # 找到合适的位置后，跳出循环。
                        break
                    # 如果下一个链表的长度大于等于预设的最大长度，则需要继续查找下一个哈希槽。
                    else:
                        # 通过再哈希找到下一个可能的哈希槽。
                        next_slot = self._rehash(next_slot, 1)

    '''
    1、模块化与分解: 将问题分解成较小、独立的部分，这样便于理解和实现。例如，在这个例子中，我们将问题分为了几个部分：
    哈希表的负载因子判断与扩容、在当前哈希槽中添加或更新键值对、在其他哈希槽中添加或更新键值对。

    2、互斥事件: 通过使用 if-elif-else 结构，我们可以将不同的情况分成互斥的事件。在这个例子中，我们将问题分为了
    以下几个互斥的事件：当前链表中包含给定的键（更新键值对）、当前链表中不包含给定的键且长度小于最大长度（直接添加
    键值对）、当前链表中不包含给定的键且长度等于最大长度（需要在其他哈希槽中添加或更新键值对）。

    3、逻辑顺序: 确保代码的执行顺序符合问题的实际逻辑。例如，在这个例子中，我们首先检查负载因子，然后在当前哈希槽
    的链表中查找键值对，最后在其他哈希槽的链表中查找键值对。这种顺序确保了我们在找到合适的位置之前，不会对哈希表进
    行不必要的扩容操作。

    '''

    def get(self, key):
        index = self._hash(key)
        linked_list = self.table[index]
        node = linked_list.find(key)

        if node:
            return node.value
        else:
            return None

    def delete(self, key):
        index = self._hash(key)
        linked_list = self.table[index]
        node = linked_list.find(key)

        if node:
            linked_list.remove(node)
            self.num_elements -= 1
        else:
            raise KeyError("Key not found")


# 创建一个空的哈希表
hash_table = HashTable()

# 向哈希表中添加键值对
hash_table.put("apple", 3)
hash_table.put("banana", 5)
hash_table.put("orange", 7)

# 使用 [] 语法添加键值对
hash_table["grape"] = 9

# 获取键值对并打印
print(f"apple: {hash_table.get('apple')}")
print(f"banana: {hash_table.get('banana')}")
print(f"orange: {hash_table.get('orange')}")

# 使用 [] 语法获取键值对并打印
print(f"grape: {hash_table['grape']}")

# 更新已有的键值对
hash_table.put("apple", 6)
print(f"Updated apple: {hash_table.get('apple')}")

# 删除键值对
del hash_table["banana"]

# 尝试访问已删除的键值对
print(f"Deleted banana: {hash_table.get('banana')}")

# 测试键是否存在于哈希表中
print(f"Does 'orange' exist?: {'orange' in hash_table}")
print(f"Does 'banana' exist?: {'banana' in hash_table}")

# 测试哈希表长度
print(f"Length of hash_table: {len(hash_table)}")

# 添加大量数据以测试动态调整大小功能
for i in range(1000):
    hash_table[f"key_{i}"] = i

# 输出调整后的哈希表大小
print(f"Resized hash_table size: {hash_table.size}")

# 验证元素是否正确存储
for i in range(1000):
    key = f"key_{i}"
    value = hash_table.get(key)
    assert value == i, f"Expected {i} for key '{key}', but got {value}"

print("All tests passed.")