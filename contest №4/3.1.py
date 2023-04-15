import random


class Node:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.size = 1
        self.left = None
        self.right = None

    def get_size(self, node):
        if node is None:
            return 0
        return node.size

    def k_max(self, k):
        if self.get_size(self.right) == k - 1:
            return self.key
        elif self.get_size(self.right) >= k:
            return self.right.k_max(k)
        else:
            return self.left.k_max(k - self.get_size(self.right) - 1)


class CartesianTree:
    def __init__(self):
        self.root = None

    def update_size(self, node):
        if node is None:
            return
        node.size = 1
        if node.left is not None:
            node.size += node.left.size
        if node.right is not None:
            node.size += node.right.size

    def split(self, node, key):
        if node is None:
            return None, None
        if node.key <= key:
            left, right = self.split(node.right, key)
            node.right = left
            self.update_size(node)
            return node, right
        else:
            left, right = self.split(node.left, key)
            node.left = right
            self.update_size(node)
            return left, node

    def merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        if left.priority >= right.priority:
            left.right = self.merge(left.right, right)
            self.update_size(left)
            return left
        else:
            right.left = self.merge(left, right.left)
            self.update_size(right)
            return right

    def add(self, key, priority):
        node = Node(key, priority)
        if self.root is None:
            self.root = node
        else:
            left, right = self.split(self.root, key)
            self.root = self.merge(self.merge(left, node), right)
        return node

    def delete(self, key):
        left, right = self.split(self.root, key - 1)
        mid, right = self.split(right, key)
        self.root = self.merge(left, right)

    def size(self, node):
        return node.size if node is not None else 0

    def rank(self, key):
        node = self.root
        rank = 0
        while node is not None:
            if node.key == key:
                return rank + self.size(node.left)
            elif node.key < key:
                rank += self.size(node.left) + 1
                node = node.right
            else:
                node = node.left
        return rank

    def select(self, rank):
        node = self.root
        while node is not None:
            left_size = self.size(node.left)
            if rank == left_size:
                return node.key
            elif rank < left_size:
                node = node.left
            else:
                rank -= left_size + 1
                node = node.right
        return None

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

    def print_inorder(self, node):
        if node is None:
            return
        self.print_inorder(node.left)
        print(node.key, end=" ")
        self.print_inorder(node.right)

    def get_inorder(self, node, list_tree):
        if node is None:
            return
        self.get_inorder(node.left, list_tree)
        list_tree.append(node.key)
        self.get_inorder(node.right, list_tree)
        return list_tree

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
        self.print_inorder(self.root)

    def get_tree_sum(self, l, r):
        _1, _2 = self.split(self.root, l)
        need, _3 = self.split(_2, r)
        return sum(self.get_inorder(need, []))

    def k_max(self, k):
        if self.root is None:
            return None
        return self.root.k_max(k)

tree = CartesianTree()
after_question = False
memory = 0
n = int(input())
for i in range(n):
    task = input().split(" ")
    if task[0] == "+":
        if after_question:
            tree.add((int(task[1]) + memory[0]) % 10 ** 9, random.random())
        else:
            tree.add(int(task[1]), random.random())
        after_question = False
    else:
        after_question = True
        memory = tree.get_tree_sum(int(task[1]), int(task[2]))
        print(memory)