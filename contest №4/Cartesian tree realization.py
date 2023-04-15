class Node:
    def __init__(self, x, y):
        self.right = None
        self.left = None
        self.x = x
        self.y = y


class Treap:
    root = None

    def split(self, x):
        if self.root is None:
            return None, None
        if self.root.x < x:
            if self.root.right is None:
                self.root.right = Treap()

            l, r = self.root.right.split(x)
            self.root.right = l
            return self.root, r
        else:
            if self.root.right is None:
                self.root.right = Treap()
            if self.root.left is None:
                self.root.left = Treap()
            l, r = self.root.left.split(x)
            self.root.left = r
            return l, self.root


    def merge(self, l, r):
        if l is None:
            return r
        if r is None:
            return l
        if  l.y < r.y:
            l.right = self.merge(l.right, r)
            return l
        else:
            r.l = self.merge(l, r.left)
            return r


    def insert(self, x, y):
        if self is None:
            return Node(x, y)
        if self.root is None:
            self.root = Node(x, y)
            return
        if self.root.y < y:
            res = self.split(x)
            new_root = Node(x, y)
            new_root.left = res[0]
            new_root.right = res[1]
            return new_root
        else:
            if self.root.x < x:
                if self.root.right is None:
                    self.root.right = Node(x, y)
                    return
                self.root.right = self.root.right.insert(x, y)
            else:
                if self.root.left is None:
                    self.root.left = Node(x, y)
                    return
                self.root.left = self.root.left.insert(x, y)


    def insert2(self, x, y):
        less, greater = self.split(x)
        self.root = self.merge(self.merge(less, Node(x, y)), greater)

    def next(self, x, flag=True):
        res = -1
        if self.left:
            res, flag = self.left.next(x, flag)
        if x <= self.x and flag:
            flag = False
            res = self.x
        if self.right:
            res, flag = self.right.next(x, flag)
        return res, flag

    def print(self):
        if self.root.left:
            self.root.left.print()
        print(self.root.x, end=" ")
        if self.root.right:
            self.root.right.print()


tree = Treap()
tree.insert2(9, 9)
tree.insert2(7, 4)
tree.insert2(3, 2)
tree.insert2(1, 4)
tree.insert2(12, 1)
tree.print()
x = 5