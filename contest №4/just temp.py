from random import random


class Node:
    def __init__(self, x, y):
        self.left = None
        self.right = None
        self.x = x
        self.y = y


    def print(self):
        if self.left:
            self.left.print()
        print(self.x, end=" ")
        if self.right:
            self.right.print()


    # def next(self, x, flag=True):
    #     res = -1
    #     if self.left:
    #         res, flag = self.left.next(x, flag)
    #     if x <= self.x and flag:
    #         flag = False
    #         res = self.x
    #     if self.right:
    #         res, flag = self.right.next(x, flag)
    #     return res, flag

    def find_min(self):
        if self is None:
            return -1
        if self.left is None:
            return self.x
        return self.left.find_min()

    def find(self, x):
        if self.x == x:
            return True
        if x < self.x:
            if self.left is None:
                return None
            return self.left.find(x)
        else:
            if self.right is None:
                return None
            return self.right.find(x)



class Treap:
    def __init__(self):
        self.root = None

    def split(self, n: Node, x):
        if n is None:
            return (None, None)
        if x < n.x:
            l, n.left = self.split(n.left, x)
            r = n
            return (l, r)
        else:
            n.right, r = self.split(n.right, x)
            l = n
            return (l, r)


    def merge(self, l, r):
        if l is None:
            return r
        if r is None:
            return l
        if l.y > l.y:
            l.right = self.merge(l.right, r)
            return l
        else:
            r.left = self.merge(l, r.left)
            return r

    def find(self, x):
        if self.root is None:
            return None
        return self.root.find(x)


    def add(self, x, y):
        if self.root is None:
            self.root = Node(x, y)
        if self.find(x) != True:
            l, r = self.split(self.root, x)
            self.root = self.merge(self.merge(l, Node(x, y)), r)


    def find_min(self):
        if self.root is None:
            return -1
        return self.root.find_min()
        # if self.root is None:
        #     return -1
        # if self.root.left is None:
        #     return self.root.x
        # return self.root.left.find_min()



    def print(self):
        if self.root is None:
            return None
        self.root.print()


    def next(self, x):
        l, r = self.split(self.root, x)
        r_min = r.find_min()
        print(r_min)
        self.root = self.merge(l, r)


tree = Treap()
after_question = False
memory = 0
n = int(input())
for i in range(n):
    task = input().split(" ")
    if task[0] == "+":
        if after_question:
            tree.add((int(task[1]) + memory) % 10 ** 9, random())
        else:
            tree.add(int(task[1]), random())
        after_question = False
    else:
        after_question = True
        memory = tree.next(int(task[1]))
        print(memory)

tree.print()

# многопотворяющиеся ? + ? + ? +
# добавление одинаковых (+-)
# -1 % 10 ** 9 (-)
# краевые случаи


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
