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



class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [LinkedList() for _ in range(self.size)]
        self.num_elements = 0
        self.max_length = 10

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        linked_list = self.table[index]
        node = linked_list.find(key)

        if node:
            node.value = value
        else:
            linked_list.append(key, value)
            self.num_elements += 1

            if len(linked_list) > self.max_length:
                self._resize()

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

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __delitem__(self, key):
        self.delete(key)

    def __contains__(self, key):
        return self.get(key) is not None

    def __len__(self):
        return self.num_elements

    def __iter__(self):
        for linked_list in self.table:
            current = linked_list.head
            while current:
                yield current.key
                current = current.next



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

