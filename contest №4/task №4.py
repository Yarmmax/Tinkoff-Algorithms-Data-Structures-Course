import sys
from random import randint


class Node:
    def __init__(self, key):
        self.key = key
        self.priority = randint(0, 10 ** 9)
        self.sum = key
        self.left = None
        self.right = None


def sum(node):
    return node.sum if node else 0


def update(node):
    if node:
        node.sum = sum(node.left) + node.key + sum(node.right)


def merge(left, right):
    if not left or not right:
        return left or right
    if left.priority > right.priority:
        left.right = merge(left.right, right)
        update(left)
        return left
    else:
        right.left = merge(left, right.left)
        update(right)
        return right


def split(node, key):
    if not node:
        return None, None
    if node.key <= key:
        left, node.right = split(node.right, key)
        update(node)
        return node, left
    else:
        node.left, right = split(node.left, key)
        update(node)
        return right, node


def insert(root, key):
    left, right = split(root, key)
    return merge(merge(left, Node(key)), right)


def get_sum(root, l, r):
    left, middle = split(root, l - 1)
    middle, right = split(middle, r)
    res = sum(middle)
    root = merge(left, merge(middle, right))
    return res, root


def main():
    root = None
    y = 0
    for line in sys.stdin.readlines()[1:]:
        if line[0] == '+':
            i = int(line[2:])
            if y != 0:
                i = (i + y) % (10 ** 9)
            root = insert(root, i)
        else:
            l, r = map(int, line[2:].split())
            res, root = get_sum(root, l, r)
            print(res)
            y = res


if __name__ == '__main__':
    main()
