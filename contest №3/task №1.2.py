def do_operations(_1, _2, op):
    if op == "+":
        return _1 + _2
    if op == "*":
        return _1 * _2
    if op == "-":
        return _2 - _1


line = input().split(" ")
for i in range(len(line)):
    if line[i].isdigit():
        line[i] = int(line[i])
stack = list()
flag = True
i = len(line) - 1
calc_place = 0
while flag:
    if i > -1:
        stack.append(line[i])
        calc_place += 1
        i -= 1
    if len(stack) > 2:
        while type(stack[len(stack)-1])  == int and type(stack[len(stack)-2])  == int:
            if stack[calc_place - 3] == "+":
                stack[calc_place - 3] = stack.pop(calc_place - 2) + stack.pop(calc_place - 2)
                calc_place -= 2
                if calc_place == 1:
                    flag = False
                    break
            if stack[calc_place - 3] == "-":
                stack[calc_place - 3] = stack.pop(calc_place - 1) - stack.pop(calc_place - 2)
                calc_place -= 2
                if calc_place == 1:
                    flag = False
                    break
            if stack[calc_place - 3] == "*":
                stack[calc_place - 3] = stack.pop(calc_place - 2) * stack.pop(calc_place - 2)
                calc_place -= 2
                if calc_place == 1:
                    flag = False
                    break
    # print(stack)
    if type(stack[0]) == int:
        flag = False
print(*stack)
# 1 2 + 3 4 + +
# 1 2 + 3 4 + 7 8 + + +
# 1 2 3 + 4 * +
# ABC + D * +  == A + (B+C) * D :  1 2 3 + 4 * + == 1 + (2 + 3) * 4 == 1 + 20 == 21 est'!