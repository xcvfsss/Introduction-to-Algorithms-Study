# 定义了一个名为TreeNode的类，表示二叉树的节点。
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 定义了一个名为BinarySearchTree的类，表示一个二叉搜索树。
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # 定义了一个名为insert的方法，用于向二叉搜索树中插入一个值。
    def insert(self, value):
        # 判断根节点是否为空。
        if self.root is None:
            # 如果根节点为空，则创建一个新的TreeNode节点作为根节点。
            self.root = TreeNode(value)
        # 如果根节点不为空，则执行下面的代码。
        else:
            # 递归地在树中插入值。
            self._insert_recursive(self.root, value)

    # 定义了一个名为_insert_recursive的私有方法，用于递归地插入值。
    def _insert_recursive(self, node, value):
        # 判断插入值是否小于当前节点的值。
        if value < node.value:
            # 判断当前节点的左子节点是否为空。
            if node.left is None:
                # 如果左子节点为空，创建一个新的TreeNode节点作为当前节点的左子节点。
                node.left = TreeNode(value)
            # 如果左子节点不为空，则执行下面的代码。
            else:
                # 在当前节点的左子树中递归地插入值。
                self._insert_recursive(node.left, value)
        # 如果插入值不小于当前节点的值，则执行下面的代码。
        else:
            # 判断当前节点的右子节点是否为空。
            if node.right is None:
                # 如果右子节点为空，创建一个新的TreeNode节点作为当前节点的右子节点。
                node.right = TreeNode(value)
            # 如果右子节点不为空，则执行下面的代码。
            else:
                # 在当前节点的右子树中递归地插入值。
                self._insert_recursive(node.right, value)

    # 定义了一个名为find的方法，用于在二叉搜索树中查找一个值。
    def find(self, value):
        # 在树中递归地查找值并返回结果。
        return self._find_recursive(self.root, value)

    # 定义了一个名为_find_recursive的私有方法，用于递归地查找值。
    def _find_recursive(self, node, value):
        # 判断当前节点是否为空，或者当前节点的值是否等于要查找的值。
        if node is None or node.value == value:
            # 如果当前节点为空或者找到了要查找的值，返回当前节点。
            return node

        # 判断查找的值是否小于当前节点的值。
        if value < node.value:
            # 如果查找的值小于当前节点的值，在当前节点的左子树中递归地查找。
            return self._find_recursive(node.left, value)
        # 如果查找的值不小于当前节点的值，则执行下面的代码。
        else:
            # 在当前节点的右子树中递归地查找。
            return self._find_recursive(node.right, value)

    # 定义了一个名为delete的方法，用于在二叉搜索树中删除一个值。
    def delete(self, value):
        # 递归地删除值并更新根节点。
        self.root = self._delete_recursive(self.root, value)

    # 定义了一个名为_delete_recursive的私有方法，用于递归地删除值。
    def _delete_recursive(self, node, value):
        # 判断当前节点是否为空。
        if node is None:
            # 如果当前节点为空，则返回当前节点。
            return node

        # 判断要删除的值是否小于当前节点的值。
        if value < node.value:
            # 如果要删除的值小于当前节点的值，在当前节点的左子树中递归地删除。
            node.left = self._delete_recursive(node.left, value)
        # 如果要删除的值大于当前节点的值，则执行下面的代码。
        elif value > node.value:
            # 在当前节点的右子树中递归地删除。
            node.right = self._delete_recursive(node.right, value)
        # 如果当前节点的值等于要删除的值，则执行下面的代码。
        else:
            # 判断当前节点的左子节点是否为空。
            if node.left is None:
                # 如果左子节点为空，返回当前节点的右子节点。
                return node.right
            # 如果当前节点的右子节点为空，则执行下面的代码。
            elif node.right is None:
                # 返回当前节点的左子节点。
                return node.left
            # 找到当前节点右子树中的最小值，并将当前节点的值替换为该最小值。
            node.value = self._find_min(node.right)
            # 在当前节点的右子树中递归地删除替换后的值。
            node.right = self._delete_recursive(node.right, node.value)

        return node

    # 定义了一个名为_find_min的私有方法，用于查找以给定节点为根的子树中的最小值。
    def _find_min(self, node):
        # 当当前节点的左子节点不为空时，继续执行循环。
        while node.left is not None:
            # 将当前节点更新为其左子节点。
            node = node.left
        # 返回找到的最小值。
        return node.value

    # 定义了一个名为inorder_traversal的方法，用于进行二叉搜索树的中序遍历。
    def inorder_traversal(self):
        # 初始化一个空列表，用于存储遍历的结果。
        result = []
        # 从根节点开始，递归地进行中序遍历。
        self._inorder_recursive(self.root, result)
        # 返回中序遍历的结果。
        return result

    # 定义了一个名为_inorder_recursive的私有方法，用于递归地进行中序遍历。
    def _inorder_recursive(self, node, result):
        # 判断当前节点是否存在。
        if node:
            # 如果当前节点存在，先遍历当前节点的左子树。
            self._inorder_recursive(node.left, result)
            # 将当前节点的值添加到结果列表中。
            result.append(node.value)
            # 遍历当前节点的右子树。
            self._inorder_recursive(node.right, result)


# 示例
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("中序遍历: ", bst.inorder_traversal())

print("查找值为 40 的节点: ", bst.find(40))

bst.delete(20)
print("删除值为 20 的节点后的中序遍历: ", bst.inorder_traversal())

bst.delete(30)
print("删除值为 30 的节点后的中序遍历: ", bst.inorder_traversal())

bst.delete(50)
print("删除值为 50 的节点后的中序遍历: ", bst.inorder_traversal())
