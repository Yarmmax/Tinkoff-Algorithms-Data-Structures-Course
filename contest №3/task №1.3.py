def do_operations(_1, _2, op):
    if op == "+":
        return _1 + _2
    if op == "*":
        return _1 * _2
    if op == "-":
        return _1 - _2


line = input().split(" ")
stack = list()
for token in line:
    if token.isdigit():
        stack.append(int(token))
    else:
        _2 = stack.pop()
        _1 = stack.pop()
        stack.append(do_operations(_1, _2, token))
print(*stack)
# 1 2 + 3 4 + +
# 1 2 + 3 4 + 7 8 + + +
# 1 2 3 + 4 * +
# 8 9 + 1 7 - *