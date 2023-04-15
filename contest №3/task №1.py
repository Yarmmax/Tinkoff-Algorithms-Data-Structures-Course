line = input().split(" ")
for i in range(len(line)):
    if line[i].isdigit():
        line[i] = int(line[i])
stack = list()
temp_stack = line[::-1]
stack = ["a"]
while not type(stack[0]) == int:
    dig_counter = 0
    sign_counter = 0
    op_counter = 0
    stack = list()
    calc_place = 0
    for i in range(len(temp_stack)):
        if type(temp_stack[i]) == int:
            dig_counter += 1
        else:
            dig_counter = 0
            sign_counter += 1
        stack.append(temp_stack[i])
        calc_place += 1
        if dig_counter == 2:
            # while
            if stack[calc_place-3] == "+":
                stack[calc_place-3] = stack.pop(calc_place-2) + stack.pop(calc_place-2)
            if stack[calc_place - 3] == "*":
                stack[calc_place - 3] = stack.pop(calc_place - 2) * stack.pop(calc_place - 2)
            if stack[calc_place - 3] == "-":
                stack[calc_place - 3] = stack.pop(calc_place - 1) - stack.pop(calc_place - 2)
    print(stack)
    temp_stack = stack.copy()
print(*stack)
# 1 2 + 3 4 + +
# 1 2 + 3 4 + 7 8 + + +
# 1 2 3 + 4 * +
# ABC + D * +  == A + (B+C) * D :  1 2 3 + 4 * + == 1 + (2 + 3) * 4 == 1 + 20 == 21 est'!