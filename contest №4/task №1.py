import random

class Node:
    def __init__(self, key=None, priority=None, left=None, right=None):
        self.key = key
        self.priority = priority if priority is not None else random.random()
        self.left = left
        self.right = right

class CartesianTree:
    def __init__(self):
        self.root = None

    def split(self, root, key):
        if root is None:
            return None, None
        elif root.key <= key:
            left, right = self.split(root.right, key)
            root.right = left
            if left is not None:
                left.parent = root
            return root, right
        else:
            left, right = self.split(root.left, key)
            root.left = right
            if right is not None:
                right.parent = root
            return left, root

    def merge(self, left, right):
        if left is None:
            return right
        elif right is None:
            return left
        elif left.priority > right.priority:
            left.right = self.merge(left.right, right)
            if left.right is not None:
                left.right.parent = left
            return left
        else:
            right.left = self.merge(left, right.left)
            if right.left is not None:
                right.left.parent = right
            return right

    def add(self, key):
        node = self.root
        parent = None
        while node is not None and node.key != key:
            parent = node
            if node.key < key:
                node = node.right
            else:
                node = node.left
        if node is not None:
            return node
        new_node = Node(key, random.random())
        if parent is None:
            self.root = new_node
        elif parent.key < key:
            parent.right = new_node
            new_node.parent = parent
        else:
            parent.left = new_node
            new_node.parent = parent
        return new_node

    def delete(self, key):
        if not self.search(key):
            return
        left, right = self.split(self.root, key-1)
        _, right = self.split(right, key)
        self.root = self.merge(left, right)
        if self.root is not None:
            self.root.parent = None

    def search(self, key):
        node = self.root
        while node is not None:
            if node.key == key:
                return True
            elif node.key < key:
                node = node.right
            else:
                node = node.left
        return False

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.key, end=" ")
        self.inorder(node.right)

    def next(self, i):
        node = self.root
        result = None
        while node is not None:
            if node.key >= i and (result is None or node.key < result.key):
                result = node
            if node.key < i:
                node = node.right
            else:
                node = node.left
        if result is None:
            return -1
        else:
            return result.key

    def print(self):
        self.inorder(self.root)

    def k_max(self, k):
        if k > self.size() or k <= 0:
            return -1
        node = self.root
        while node is not None:
            right_size = 0 if node.right is None else node.right.subtree_size
            if k == right_size + 1:
                return node.key
            elif k <= right_size:
                node = node.right
            else:
                k = k - right_size - 1
                node = node.left
        return -1


tree = CartesianTree()
after_question = False
memory = 0
n = int(input())
for i in range(n):
    task = input().split(" ")
    if task[0] == "+":
        if after_question:
            tree.add((int(task[1]) + memory) % 10 ** 9)
        else:
            tree.add(int(task[1]))
        after_question = False
    else:
        after_question = True
        memory = tree.next(int(task[1]))
        print(memory)

# tree.print()

# 15
# + 1
# + 2
# + 3
# + 4
# ? 2
# 2
# ? 3
# 3
# ? 4
# 4
# + 123
# ? 23
# 127
# ? 22
# 127
# ? 3
# 3
# + 123


# 15
# + 1
# + 2
# + 3
# ? 2
# 2
# + 4
# ? 3
# 3
# ? 4
# 6
# + 123
# ? 23
# 129
