class HashTable:
    def __init__(self, size = 10):
        self.size = size
        self.table = [None] * self.size
        self.load_factor = 0.6
        self.num_elements = 0

    def _hash(self, key):
        return hash(key) % self.size

    def _rehash(self, old_hash, step):
        return (old_hash + step) % self.size

    def _resize(self):
        old_table = self.table
        self.size = self.size * 2
        self.table = [None] * self.size
        self.num_elements = 0
        for item in old_table:
            if item is not None:
                self.put(item[0], item[1])

    def put(self, key, value):
        if self.num_elements / self.size > self.load_factor:
            self._resize()
        hash_value = self._hash(key)
        if self.table[hash_value] is None:
            self.table[hash_value] = (key, value)
            self.num_elements += 1
        elif self.table[hash_value][0] == key:
            self.table[hash_value] = (key, value)
        else:
            next_slot = self._rehash(hash_value, 1)
            while self.table[next_slot] is not None and self.table[next_slot][0] != key:
                next_slot = self._rehash(next_slot, 1)
            if self.table[next_slot] is None:
                self.num_elements += 1
            self.table[next_slot] = (key, value)

    def get(self, key):
        start_slot = self._hash(key)
        position = start_slot
        while self.table[position] is not None:
            if self.table[position][0] == key:
                return self.table[position][1]
            else:
                position = self._rehash(position, 1)
                if position == start_slot:
                    return None
        return None

    def __contains__(self, key):
        start_slot = self._hash(key)
        position = start_slot
        while self.table[position] is not None:
            if self.table[position][0] == key:
                return True
            else:
                position = self._rehash(position, 1)
                if position == start_slot:
                    break
        return False

    def __delitem__(self, key):
        start_slot = self._hash(key)
        position = start_slot
        while self.table[position] is not None:
            if self.table[position][0] == key:
                self.table[position] = None
                self.num_elements -= 1
                return
            else:
                position = self._rehash(position, 1)
                if position == start_slot:
                    break
        raise KeyError('Key not found')

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)



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