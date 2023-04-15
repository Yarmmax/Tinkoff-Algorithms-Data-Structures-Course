class Node:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.data = x

class Tree:
    root = None

    def insert(self, x):
        if self.root is None:
            self.root = Node(x)
            return
        if x < self.root.data:
            if self.root.left is None:
                self.root.left = Tree()
            self.root.left.insert(x)
        else:
            if self.root.right is None:
                self.root.right = Tree()
            self.root.right.insert(x)


    def find(self, x):
        if self.root is None:
            return None
        if self.root.data == x:
            return self.root
        if x < self.root.data:
            if self.root.left is None:
                return None
            return self.root.left.find(x)
        else:
            if self.root.right is None:
                return None
            return self.root.right.find(x)

    def print(self):
        if self.root.left:
            self.root.left.print()
        print(self.root.data, end=" ")
        if self.root.right:
            self.root.right.print()

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.root.right is None and self.root.left is None:
            line = '%s' % self.root.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.root.right is None:
            lines, n, p, x = self.root.left._display_aux()
            s = '%s' % self.root.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.root.left is None:
            lines, n, p, x = self.root.right._display_aux()
            s = '%s' % self.root.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.root.left._display_aux()
        right, m, q, y = self.root.right._display_aux()
        s = '%s' % self.root.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


tree = Tree()
tree.insert(5)
tree.insert(2)
tree.insert(8)
tree.insert(4)
tree.insert(3)
tree.insert(5)
tree.insert(4)
tree.insert(7)
tree.insert(12)
tree.insert(9)
tree.insert(10)
tree.insert(11)
tree.insert(12)
tree.print()
print()
tree.display()
#print(-1 % 10 ** 9)