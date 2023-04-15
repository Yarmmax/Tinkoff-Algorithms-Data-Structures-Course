#[9, 3, 5, 10, 2, 1, 4, 8, 6, 7]

#amount = int(input())
dataset = [9, 3, 5, 10, 2, 1, 4, 8, 6, 7] # list(map(int, input().split(" ")))\
amount = len(dataset)
stack_end = list()
stack_pad = list()
global_action_counter = 0
answer = list()
local_action_counter1 = 0
local_action_counter2 = 0
is_possible = True
is_end_empty = True
is_pad_empty = True
counter = 0
while counter < amount:
    if len(stack_end) == 0 or stack_end[-1] > dataset[counter]:
        stack_end.append(dataset[counter])
        local_action_counter1 += 1
        counter += 1
    else:
        global_action_counter += 1
        answer.append("1 " + str(local_action_counter1))
        local_action_counter1 = 0
        if not is_pad_empty:
            if stack_end[-1] != len(stack_pad)+1:
                is_possible = False
                break
            while  stack_pad[-1] + 1 == stack_end[-1]:
                stack_pad.append(stack_end.pop())
                local_action_counter2 += 1
            if len(stack_end) == 0:
                is_end_empty = True
            local_action_counter2 += 1
        if is_pad_empty:
            if stack_end[-1] != len(stack_pad)+1:
                is_possible = False
                break
            else:
                is_pad_empty = False
                stack_pad.append(stack_end.pop())
                local_action_counter2 += 1
                while len(stack_end) != 0 and stack_pad[-1] + 1 == stack_end[-1]:
                    stack_pad.append(stack_end.pop())
                    local_action_counter2 += 1
                if len(stack_end) == 0:
                    is_end_empty = True
        answer.append("2 " + str(local_action_counter2))
        local_action_counter2 = 0
        global_action_counter += 1
answer.append("1 " + str(local_action_counter1))
global_action_counter += 1
answer.append("2 " + str(len(stack_end)))
global_action_counter += 1
if is_possible:
    print(global_action_counter)
    for j in answer:
        print(*j)
else:
    print(0)