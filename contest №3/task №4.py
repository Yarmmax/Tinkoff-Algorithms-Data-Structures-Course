class Deque:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add_front(self, item):
        node = self.Node(item)
        if self.is_empty():
            self.front = node
            self.back = node
        else:
            node.next = self.front
            self.front.prev = node
            self.front = node
        self.size += 1

    def add_back(self, item):
        node = self.Node(item)
        if self.is_empty():
            self.back = node
            self.front = node
        else:
            node.prev = self.back
            self.back.next = node
            self.back = node
        self.size += 1

    def remove_front(self):
        if self.is_empty():
            return None
        item = self.front.value
        if self.size == 1:
            self.front = None
            self.back = None
        else:
            self.front = self.front.next
            self.back.prev = None
        self.size -= 1
        return item

    def remove_back(self):
        if self.is_empty():
            return None
        value = self.back.value
        if self.size == 1:
            self.front = None
            self.back = None
        else:
            self.back = self.back.prev
            self.back.next = None
        self.size -= 1
        return value

    def print(self):
        if self.is_empty():
            print("Deque is empty")
        else:
            current = self.front
            while current:
                print(current.value, end=" ")
                current = current.next
            print()

deq1 = Deque()
deq2 = Deque()
# "* 1","* 2", "* 3", "* 4", "* 5", "* 6", "* 7", "* 8", "* 9", "* 10"
# "+ 1","+ 2", "-", "+ 3", "+ 4", "-", "-"
# "+ 1","+ 2", "-", "+ 3", "+ 4", "-", "-"
# "+ 1","+ 2", "* 3", "-","* 5", "* 5", "-", "* 7", "* 8", "-", "* 10", "* 11", "* 12", "* 13", "* 14", "-"
# f_test = ["+ 1","+ 2", "-", "+ 3", "+ 4", "-", "-"]
#n = int(input()) #  len(test)#
#test = list(input().split(" ")) # [1, 2, 3, 4, 5]
test =["+ 1","+ 2","+ 3","+ 4","+ 5","* 6"]
# +1+2+3+4+5*6
# "+ 1","+ 2","+ 3","+ 4","+ 5","* 6"
n = len(test)
for _ in range(n):
    item = test[_]
    op = item[0]
    value = item[2:]
    if op == "+":
        # 1
        if deq1.size > deq2.size:
            deq2.add_back(value)
            deq1.print(); deq2.print();print()
        # 2
        else:
            deq2.add_back(value)
            shift = deq2.remove_front()
            deq1.add_back(shift)
            deq1.print();deq2.print();print()
    elif op == "*":
        # 3
        if (deq1.size + deq2.size) % 2 == 0:
            deq1.add_back(value)
            deq1.print();deq2.print();print()
        # 4
        else:
            deq2.add_front(value)
            deq1.print();deq2.print();print()
            #if deq1.size - deq2.size == 2:
                #shift = deq1.remove_back()
                #deq2.add_front(shift)
    else:
        # 5
        answer = deq1.remove_front()
        print(answer)
        if deq2.size - deq1.size == 1:
            shift = deq2.remove_front()
            deq1.add_back(shift)
        deq1.print();deq2.print();print()